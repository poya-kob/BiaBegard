# Generated by Django 3.2.6 on 2021-09-12 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_auto_20210911_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsgalleries',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='content.products', verbose_name='محصول مربوطه'),
        ),
    ]
