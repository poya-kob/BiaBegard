from django.db import models
from django.contrib.auth.models import User

from django_jalali.db import models as jmodels
from content.models import Products


class Comments(models.Model):

    title = models.CharField(max_length=150, verbose_name='عنوان نظر')
    description = models.TextField(verbose_name="متن اصلی نظر")

    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, verbose_name="کاربر مربوطه")
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name="پاسخ به",
                              related_name='comment_reply')
    created_time = jmodels.jDateTimeField(auto_now_add=True, verbose_name='زمان ایجاد نظر')
    active = models.BooleanField(default=False, verbose_name='فعال / غیر فعال')
    product = models.ForeignKey(Products,on_delete=models.CASCADE, verbose_name='محصولات', related_name='comments', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"
