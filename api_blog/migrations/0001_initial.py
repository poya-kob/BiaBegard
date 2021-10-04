# Generated by Django 3.2.6 on 2021-10-03 15:08

import ckeditor_uploader.fields
from django.db import migrations, models
import utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان مطلب')),
                ('image', models.ImageField(upload_to=utils.upload_image_path, verbose_name='بنر خبر -398*862-')),
                ('active', models.BooleanField(default=False, verbose_name='فعال/غیرفعال')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد پست')),
                ('description', models.TextField(max_length=690, verbose_name='توضیحات کوتاه(یک پاراگراف)')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='متن خبر')),
            ],
            options={
                'verbose_name': 'خبر',
                'verbose_name_plural': 'اخبار',
            },
        ),
    ]
