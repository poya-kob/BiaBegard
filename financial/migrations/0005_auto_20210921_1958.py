# Generated by Django 3.2.6 on 2021-09-21 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0004_auto_20210921_1010'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartitems',
            options={'verbose_name': 'آیتم کارت', 'verbose_name_plural': 'آیتم های کارت'},
        ),
        migrations.AlterModelOptions(
            name='carts',
            options={'verbose_name': 'کارت', 'verbose_name_plural': 'کارت ها'},
        ),
        migrations.DeleteModel(
            name='Invoice',
        ),
    ]