# Generated by Django 3.2.6 on 2021-11-05 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iran_zone', '0002_auto_20211105_1231'),
        ('account', '0004_auto_20211023_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='addresses',
            name='township',
            field=models.ForeignKey(default=122, on_delete=django.db.models.deletion.CASCADE, to='iran_zone.shahrestan', verbose_name='شهرستان'),
        ),
        migrations.AddField(
            model_name='addresses',
            name='village',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='iran_zone.dehestan', verbose_name='روستا'),
        ),
        migrations.AddField(
            model_name='addresses',
            name='zip_code',
            field=models.PositiveBigIntegerField(null=True, verbose_name='کد پستی'),
        ),
        migrations.AlterField(
            model_name='addresses',
            name='city',
            field=models.ForeignKey(default=394, on_delete=django.db.models.deletion.CASCADE, to='iran_zone.shahr', verbose_name='شهر'),
        ),
        migrations.AlterField(
            model_name='addresses',
            name='full_address',
            field=models.CharField(max_length=200, verbose_name='آدرس کامل'),
        ),
        migrations.AlterField(
            model_name='addresses',
            name='province',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, to='iran_zone.ostan', verbose_name='استان'),
        ),
        migrations.RemoveField(
            model_name='customers',
            name='address',
        ),
        migrations.AddField(
            model_name='customers',
            name='address',
            field=models.ManyToManyField(to='account.Addresses', verbose_name='آدرس های کاربر'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='phone',
            field=models.PositiveBigIntegerField(null=True, verbose_name='تلفن همراه'),
        ),
        migrations.RemoveField(
            model_name='suppliers',
            name='address',
        ),
        migrations.AddField(
            model_name='suppliers',
            name='address',
            field=models.ManyToManyField(to='account.Addresses', verbose_name='آدرس های کاربر'),
        ),
        migrations.AlterField(
            model_name='suppliers',
            name='phone',
            field=models.PositiveBigIntegerField(null=True, verbose_name='تلفن همراه'),
        ),
    ]
