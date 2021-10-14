# Generated by Django 3.2.6 on 2021-10-08 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210910_1905'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'مشترک',
                'verbose_name_plural': 'مشترکین',
            },
        ),
    ]