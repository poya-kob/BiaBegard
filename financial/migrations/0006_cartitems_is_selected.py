# Generated by Django 3.2.6 on 2021-09-22 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0005_auto_20210921_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitems',
            name='is_selected',
            field=models.BooleanField(default=False, verbose_name='انتخاب'),
        ),
    ]