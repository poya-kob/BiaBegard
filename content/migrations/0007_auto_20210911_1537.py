# Generated by Django 3.2.6 on 2021-09-11 11:07

from django.db import migrations, models
import utils


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_auto_20210910_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='brands',
            name='image',
            field=models.ImageField(null=True, upload_to=utils.upload_image_path, verbose_name='لوگوی برند'),
        ),
        migrations.AlterField(
            model_name='brands',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='نام برند'),
        ),
    ]
