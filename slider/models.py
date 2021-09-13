from django.db import models
from utils import upload_image_path

# Create your models here.


class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    link = models.URLField(max_length=250, verbose_name='آدرس')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to=upload_image_path, blank=True, null=True, verbose_name="تصاویر اسلایدر")

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = "اسلایدرها"

    def __str__(self):
        return self.title
