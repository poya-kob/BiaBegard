# Generated by Django 3.2.6 on 2021-10-03 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_blog', '0003_alter_blog_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='نام دسته بندی')),
            ],
        ),
    ]
