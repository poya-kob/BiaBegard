from django.db import models
from django.contrib.auth.models import User

from utils import upload_image_path
from iran_zone.models import Ostan, Shahrestan, Dehestan, Shahr


class Addresses(models.Model):
    province = models.ForeignKey(Ostan, on_delete=models.CASCADE, default=8, verbose_name="استان")
    township = models.ForeignKey(Shahrestan, on_delete=models.CASCADE, default=122, verbose_name="شهرستان")
    city = models.ForeignKey(Shahr, on_delete=models.CASCADE, default=394, verbose_name="شهر", null=True)
    village = models.ForeignKey(Dehestan, on_delete=models.CASCADE, verbose_name="روستا", null=True, blank=True)
    zip_code = models.PositiveBigIntegerField(verbose_name="کد پستی", null=True)
    full_address = models.CharField(max_length=200, verbose_name="آدرس کامل")
    is_selected = models.BooleanField(default=False, verbose_name='انتخاب شده / نشده')

    class Meta:
        verbose_name = "آدرس"
        verbose_name_plural = "آدرس ها"

    def __str__(self):
        return str(self.zip_code)

    def save(self, *arg, **kwargs):
        assert len(str(self.zip_code)) == 10, "کد پستی باید ۱۰ رقم باشد"
        super().save(*arg, **kwargs)


class CommonUsersField(User):
    image = models.ImageField(upload_to=upload_image_path, verbose_name="تصویر کاربر", null=True, blank=True)
    address = models.ManyToManyField(Addresses, verbose_name="آدرس های کاربر")
    phone = models.PositiveBigIntegerField(null=True, verbose_name="تلفن همراه")

    class Meta:
        abstract = True


class Suppliers(CommonUsersField):
    store_name = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name = "فروشنده"
        verbose_name_plural = "فروشنده ها"


class Customers(CommonUsersField):
    class Meta:
        verbose_name = "مشتری"
        verbose_name_plural = "مشتری ها"


class Subscribers(models.Model):
    email = models.EmailField(verbose_name="ایمیل")
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "مشترک"
        verbose_name_plural = "مشترکین"

    def __str__(self):
        return self.email
