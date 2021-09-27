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


# class Orders(models.Model):
#     user = models.ForeignKey(User, verbose_name="مالک سبد", on_delete=models.CASCADE)
#     is_payed = models.BooleanField(default=False, verbose_name="پرداخت شده/نشده")
#     payment_date = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت')
#     shipping = models.ForeignKey(Post, null=True, on_delete=models.CASCADE, verbose_name='پست شونده')
#     offs = models.ForeignKey(Offs, null=True, on_delete=models.CASCADE, verbose_name="کد تخفیف ")
#
#     class Meta:
#         verbose_name = 'سبد خرید'
#         verbose_name_plural = 'سبدهای خرید کاربران'
#
#     def __str__(self):
#         return self.user.username
#
#     def save(self, *args, **kwargs):
#         # اول از همه چک میکنیم این کد تخفیف وجود دارد یا نه
#         if self.offs:
#             offs_qs = Offs.objects.get(off_codes=self.offs)
#             if offs_qs:
#                 if datetime.now() > offs_qs.off_expire:
#                     raise Exception("تاریخ استفاده از این کد به اتمام رسیده است.")
#
#                 if offs_qs.number_off <= 0:
#                     raise Exception("تعداد استفاده از این کد به اتمام رسیده است")
#
#                 # user  همان یوزی است که در تیبل ذخیره داریم و
#                 # self.user  همان یوزر فعلی ماست که قصد خرید دارد
#                 # بین سبدهای خرید میگردیم ببینیم یوزر فعلی ما این کد فعلی را استفاده کرده یا نکرده
#                 if Orders.objects.filter(user=self.user, offs=offs_qs).count() <= 0:
#                     offs_qs.number_off -= 1
#                     offs_qs.save()
#             else:
#                 raise Exception(' این کد قابل استفاده نیست ')
#         else:
#             return super().save(*args, **kwargs)


# class OrderDetails(models.Model):
#     product = models.ForeignKey(Products, verbose_name="محصول", on_delete=models.CASCADE)
#     number_of_products = models.IntegerField(verbose_name="تعداد محصول")
#     order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='order_detail', verbose_name="سبد خرید")
#
#     @property
#     def total_price_product(self):
#         if self.product.off_price and self.product.off_expired_time >= datetime.now():
#             return self.product.off_price * self.number_of_products
#         else:
#             return self.product.product_price * self.number_of_products
#
#     def __str__(self):
#         return self.product.name
#
#     class Meta:
#         verbose_name = 'جزئیات پرداخت'
#         verbose_name_plural = 'جزئیات پرداخت'


class Carts(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="کاربر مربوطه")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="زمان ایجاد کارت")
    update_at = models.DateTimeField(auto_now=True, verbose_name="زمان اخرین تغییرات")

    class Meta:
        verbose_name = "کارت"
        verbose_name_plural = "کارت ها"

    def __str__(self):
        return self.user.username


class CartItems(models.Model):
    STATUS_CHOICES = (
        ('paid', 'پرداخت شده'),
        ('pending', 'منتظر پرداخت')
    )
    cart = models.ForeignKey(Carts, on_delete=models.CASCADE, related_name="cart_items", verbose_name="کارت مربوطه")
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name="محصول مربوطه")
    qty = models.PositiveIntegerField(default=1, verbose_name="تعداد از محصول")
    status = models.CharField(verbose_name="وضعیت پرداخت", choices=STATUS_CHOICES, max_length=7, default="pending")
    is_selected = models.BooleanField(default=False, verbose_name='انتخاب')

    class Meta:
        verbose_name = "آیتم کارت"
        verbose_name_plural = "آیتم های کارت"

    def __str__(self):
        return self.product.name

    def save(self, *args, **kwargs):
        if self.product.inventory < self.qty:
            raise Exception("تعداد وارد شده بیشتر از موجودی میباشد")

        super().save(*args, **kwargs)

    @property
    def total_price_product(self):
        if self.product.off_price and self.product.off_expired_time >= datetime.now():
            return self.product.off_price * self.qty
        else:
            return self.product.product_price * self.qty
