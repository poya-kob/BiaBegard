# Generated by Django 3.2.6 on 2021-09-10 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='addresses',
            options={'verbose_name': 'آدرس', 'verbose_name_plural': 'آدرس ها'},
        ),
        migrations.AlterModelOptions(
            name='customers',
            options={'verbose_name': 'مشتری', 'verbose_name_plural': 'مشتری ها'},
        ),
        migrations.AlterModelOptions(
            name='suppliers',
            options={'verbose_name': 'فروشنده', 'verbose_name_plural': 'فروشنده ها'},
        ),
    ]
