from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
from utils import upload_image_path


class SiteSetting(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان سایت")
    logo = models.ImageField(upload_to=upload_image_path, verbose_name="لوگوی سایت")
    about_us = RichTextUploadingField(verbose_name="درباره سایت")
    address = models.TextField(verbose_name="آدرس سایت")
    telephone = models.PositiveBigIntegerField(verbose_name="تلفن سایت")
    mobile = models.PositiveBigIntegerField(verbose_name="تلفن همراه")
    fax = models.PositiveBigIntegerField(verbose_name="فکس", null=True, blank=True)
    email = models.EmailField(null=True, blank=True, verbose_name="ایمیل سایت")

    class Meta:
        verbose_name = "تنطیمات سایت"
        verbose_name_plural = "تنطیمات سایت"
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if SiteSetting.objects.all().count() > 0:
            raise Exception("نمیتوانید بیشتر از یک تنطیمات برای سایت اضافه کنید.")
        else:
            return super().save(*args, **kwargs)
