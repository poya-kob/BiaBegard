from django.db import models
from django.contrib.auth.models import User

from utils import upload_image_path

from .manager import ProductsManager


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="نام دسته بندی")
    subcategory = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)


class Products(models.Model):
    __original_price = None
    __original_off_price = None
    name = models.CharField(max_length=150, verbose_name="نام")
    image = models.ImageField(upload_to=upload_image_path, verbose_name="کاور اصلی محصول")
    inventory = models.IntegerField(verbose_name="موجودی محصول")
    created_time = models.DateTimeField(verbose_name="زمان ایجاد محصول", auto_now_add=True)
    category = models.ManyToManyField(Category)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=False, verbose_name="فعال/غیرفعال")
    product_price = models.FloatField(verbose_name="قیمت محصول", )
    off_price = models.FloatField(verbose_name="قیمت با تخفیف", null=True, blank=True)
    off_expired_time = models.DateTimeField(verbose_name="زمان انقضاء تخفیف", null=True, blank=True)
    objects = ProductsManager()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_price = self.product_price
        self.__original_off_price = self.off_price

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.off_price <= 0 or self.off_price >= self.product_price:
            raise Exception(f"{self.off_price} نمیتواند بعوان قیمت با تخفیف محصول قرار گیرد. ")
        elif self.product_price <= 0:
            raise Exception(f"{self.product_price} نمیتواند بعوان قیمت محصول قرار گیرد. ")

        if self.off_price != self.__original_off_price:
            PricesHistory.objects.create(product=self, product_price=self.off_price)
        elif self.product_price != self.__original_price:
            PricesHistory.objects.create(product=self, product_price=self.product_price)
        super().save(force_insert, force_update, using, update_fields)


class PricesHistory(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name="محصول مربوطه",
                                related_name="product_price_history")
    product_price = models.FloatField(verbose_name="قیمت محصول", default=0)
    modified_date = models.DateField(verbose_name="زمان ثبت تغییرات قیمت", auto_now_add=True)
