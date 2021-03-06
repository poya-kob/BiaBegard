# Generated by Django 3.2.6 on 2021-08-28 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان نظر')),
                ('description', models.TextField(verbose_name='متن اصلی نظر')),
                ('type', models.CharField(choices=[('p', 'products'), ('b', 'blogs')], max_length=1, verbose_name='نظر برای محصول / بلاگ')),
                ('id_for', models.IntegerField(verbose_name='id محصول / بلاگ')),
                ('created_time', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='زمان ایجاد نظر')),
                ('active', models.BooleanField(default=False, verbose_name='فعال / غیر فعال')),
                ('reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_reply', to='comment.comments', verbose_name='پاسخ به')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='کاربر مربوطه')),
            ],
            options={
                'verbose_name': 'نظر',
                'verbose_name_plural': 'نظرات',
            },
        ),
    ]
