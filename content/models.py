from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

from utils import upload_image_path
from .manager import ProductsManager
from ckeditor_uploader.fields import RichTextUploadingField
from django_jalali.db import models as jmodels


class CategoryType(models.Model):
    type_name = models.CharField(max_length=150, verbose_name="نام نوع دسته بندی", unique=True)
    have_subcategory = models.BooleanField(default=False, verbose_name="زیر دسته بندی داشته / نداشته باشد؟")

    class Meta:
        verbose_name = "نوع دسته بندی"
        verbose_name_plural = "انواع دسته بندی"

    def __str__(self):
        return self.type_name


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="نام دسته بندی", unique=True)
    type = models.ForeignKey(CategoryType, on_delete=models.RESTRICT, verbose_name="نوع دسته بندی")
    main_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                                      verbose_name='دسته بندی والد')

    # calender = jmodels.jDateTimeField(null=True)

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.main_category is not None:
            if not self.type.have_subcategory:
                raise Exception(f" برای نوع دسته {self.type.type_name} نمیتواند زیر دسته داشته باشد. ")
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
    created_time = jmodels.jDateTimeField(verbose_name="زمان ایجاد محصول", auto_now_add=True)
    category = models.ManyToManyField(Category, verbose_name="دسته بندی مربوطه")
    supplier = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="فروشنده محصول")
    product_price = models.FloatField(verbose_name="قیمت محصول", default=0)
    off_price = models.FloatField(verbose_name="قیمت با تخفیف", null=True, blank=True, default=0)
    off_expired_time = jmodels.jDateTimeField(verbose_name="زمان انقضاء تخفیف", null=True, blank=True)
    like_count = models.IntegerField(default=0, verbose_name="تعداد لایک های محصول")
    active = models.BooleanField(default=False, verbose_name="فعال/غیرفعال")
    objects = ProductsManager()

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_price = self.product_price
        self.__original_off_price = self.off_price

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.off_price and self.off_expired_time is None:
            raise Exception("تاریخ انقضا برای پایان تخفیف تعیین کنید.")
        if self.inventory <= 0:
            raise Exception("موجودی محصول نمیتواند صفر یا کمتر از آن باشد")
        if self.product_price <= 0:
            raise Exception(f"{self.product_price} نمیتواند بعوان قیمت محصول قرار گیرد. ")
        if self.off_price < 0 or self.off_price >= self.product_price:
            raise Exception(f"{self.off_price} نمیتواند بعوان قیمت با تخفیف محصول قرار گیرد. ")
        if self.off_expired_time > datetime.now():
            raise Exception("زمان پایان تخفیف نمیتواند امروز یا الآن باشد")

        super().save(force_insert, force_update, using, update_fields)
        if self.off_price != self.__original_off_price > 0:
            PricesHistory.objects.create(product=self, product_price=self.off_price)
        elif self.product_price != self.__original_price:
            PricesHistory.objects.create(product=self, product_price=self.product_price)

    def __str__(self):
        return self.name


class PricesHistory(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name="محصول مربوطه",
                                related_name="product_price_history")
    product_price = models.FloatField(verbose_name="قیمت محصول", default=0)
    modified_date = models.DateField(verbose_name="زمان ثبت تغییرات قیمت", auto_now_add=True)


class Tags(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان')
    created_time = jmodels.jDateTimeField(auto_now_add=True, verbose_name='زمان ثبت')
    active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')
    products = models.ManyToManyField(Products, blank=True, verbose_name='محصولات')

    class Meta:
        verbose_name = 'تگ/برچسب'
        verbose_name_plural = 'تگ ها / برچسب ها'

    def __str__(self):
        return self.title


class ProductsGalleries(models.Model):
    title = models.CharField(max_length=120, verbose_name="عنوان عکس")
    image = models.ImageField(upload_to=upload_image_path, verbose_name="تصویر محصول")
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name="محصول مربوطه")
    active = models.BooleanField(default=False, verbose_name="فعال / غیر فعال")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "گالری محصول"
        verbose_name_plural = "گالری محصولات"
