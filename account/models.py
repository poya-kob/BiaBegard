from django.db import models
from django.contrib.auth.models import User

from utils import upload_image_path


class Addresses(models.Model):
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    full_address = models.CharField(max_length=200)

    class Meta:
        verbose_name = "آدرس"
        verbose_name_plural = "آدرس ها"


class CommonUsersField(User):
    image = models.ImageField(upload_to=upload_image_path, verbose_name="تصویر کاربر", null=True, blank=True)
    address = models.ForeignKey(Addresses, on_delete=models.CASCADE, null=True)
    phone = models.PositiveBigIntegerField(null=True)

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
