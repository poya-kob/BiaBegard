from django.db import models
from content.models import Products
from django.contrib.auth.models import User
from shipping.models import Post
from datetime import datetime


class Offs(models.Model):
    user_off = models.ForeignKey(User, on_delete=models.CASCADE)

    number_off = models.IntegerField(verbose_name=" تعداد دفعات مجاز استفاده از کد تخفیف")
    off_codes = models.CharField(max_length=200, unique=True, verbose_name="کدتخفیف")
    off_percentage = models.IntegerField(verbose_name="درصد تخفیف")
    off_expire = models.DateTimeField(verbose_name="تاریخ انقضاء کد")

    def save(self, *args, **kwargs):
        if self.off_percentage < 0 or self.off_percentage > 100:
            raise Exception("درصد خفیف نمیتواند از ۰ کمتر و از ۱۰۰ بیشتر باشد.")
        if self.number_off <= 0:
            raise Exception('تعداد دفعات استفاده از کد تخفیف نمیتوان ۰ یا کمتر باشد.')
        super().save(self, *args, **kwargs)

    class Meta:
        verbose_name = "کد تخفیف"
        verbose_name_plural = "کد های تخفیف"


class Orders(models.Model):
    user = models.ForeignKey(User, verbose_name="مالک سبد", on_delete=models.CASCADE)
    is_payed = models.BooleanField(default=False, verbose_name="پرداخت شده/نشده")
    payment_date = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت')
    shipping = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='پست شونده')
    offs = models.ForeignKey(Offs, on_delete=models.CASCADE, verbose_name="کد تخفیف ")

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبدهای خرید کاربران'

    def __str__(self):
        return self.user.get_full_name()

    def save(self, *args, **kwargs):
        # اول از همه چک میکنیم این کد تخفیف وجود دارد یا نه
        offs_qs = Offs.objects.get(off_codes=self.offs)
        if offs_qs:
            if datetime.now() > offs_qs.off_expire:
                raise Exception("تاریخ استفاده از این کد به اتمام رسیده است.")

            if offs_qs.number_off <= 0:
                raise Exception("تعداد استفاده از این کد به اتمام رسیده است")

            # user  همان یوزی است که در تیبل ذخیره داریم و
            # self.user  همان یوزر فعلی ماست که قصد خرید دارد
            # بین سبدهای خرید میگردیم ببینیم یوزر فعلی ما این کد فعلی را استفاده کرده یا نکرده
            if Orders.objects.filter(user=self.user, offs=offs_qs).count() <= 0:
                offs_qs.number_off -= 1
                offs_qs.save()
        else:
            raise Exception(' این کد قابل استفاده نیست ')


class OrderDetails(models.Model):
    product = models.ForeignKey(Products, verbose_name="محصول", on_delete=models.CASCADE)
    number_of_products = models.IntegerField(verbose_name="تعداد محصول")
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, verbose_name="سبد خرید")

    @property
    def total_price_product(self):
        return self.product.product_price * self.number_of_products

    class Meta:
        verbose_name = 'جزئیات پرداخت'
        verbose_name_plural = 'جزئیات پرداخت'
