# Generated by Django 3.2.6 on 2021-11-12 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iran_zone', '0002_auto_20211105_1231'),
        ('account', '0005_auto_20211105_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='addresses',
            name='is_selected',
            field=models.BooleanField(default=False, verbose_name='انتخاب شده / نشده'),
        ),
        migrations.AlterField(
            model_name='addresses',
            name='village',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='iran_zone.dehestan', verbose_name='روستا'),
        ),
    ]
