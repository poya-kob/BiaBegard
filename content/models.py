from django.db import models
from django.contrib.auth.models import User

from utils import upload_image_path
from .manager import ProductsManager
from ckeditor_uploader.fields import RichTextUploadingField


class CategoryType(models.Model):
    type_name = models.CharField(max_length=150, verbose_name="نام نوع دسته بندی")
    have_subcategory = models.BooleanField(default=False, verbose_name="زیر دسته بندی داشته / نداشته باشد؟")

    class Meta:
        verbose_name = "نوع دسته بندی"
        verbose_name_plural = "انواع دسته بندی"

    def __str__(self):
        return self.type_name


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="نام دسته بندی")
    type = models.ForeignKey(CategoryType, on_delete=models.RESTRICT)
    main_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.type.have_subcategory == False and self.main_category is not None:
            raise Exception(f"برای نوع دسته{self.type.type_name} نمیتواند زیر دسته داشته باشد.")
        elif self.main_category.type != self.type:
            raise Exception("نوع زیر دسته بندی باید با دسته بندی اصلی برابر باشد")
        super().save(force_insert, force_update, using, update_fields)


class Products(models.Model):
    __original_price = None
    __original_off_price = None
    name = models.CharField(max_length=150, verbose_name="نام")
    image = models.ImageField(upload_to=upload_image_path, verbose_name="کاور اصلی محصول")
    inventory = models.IntegerField(verbose_name="موجودی محصول")
    short_description = models.TextField(max_length=700, verbose_name="توضیحات کوتاه محصول")
    full_description = RichTextUploadingField(verbose_name="توضیحات کامل محصول")
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

    def __str__(self):
        return self.name


class PricesHistory(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name="محصول مربوطه",
                                related_name="product_price_history")
    product_price = models.FloatField(verbose_name="قیمت محصول", default=0)
    modified_date = models.DateField(verbose_name="زمان ثبت تغییرات قیمت", auto_now_add=True)
