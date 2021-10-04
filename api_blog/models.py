from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.contrib.auth.models import User
from utils import upload_image_path


class BlogCategory(models.Model):
    name = models.CharField(max_length=150, verbose_name="نام دسته بندی")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "دسته بندی ها"
        verbose_name = "دسته بندی"


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان مطلب")
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, verbose_name='نام دسته بندی')
    image = models.ImageField(upload_to=upload_image_path, verbose_name="بنر خبر -398*862-")
    active = models.BooleanField(default=False, verbose_name="فعال/غیرفعال")
    date = models.DateTimeField(auto_now_add=True, verbose_name="زمان ایجاد پست")
    description = models.TextField(verbose_name="توضیحات کوتاه(یک پاراگراف)")
    text = RichTextUploadingField(verbose_name="متن خبر", null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "اخبار"
        verbose_name = "خبر"


class Comments(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان نظر')
    description = models.TextField(verbose_name="متن اصلی نظر")
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, verbose_name="کاربر مربوطه")
    blog = models.ForeignKey(to=Blog, on_delete=models.CASCADE, related_name='comment', verbose_name="مقاله مربوطه")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد نظر')
    active = models.BooleanField(default=False, verbose_name='فعال / غیر فعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "نظرات"
        verbose_name = "نظر"
