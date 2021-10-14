# Generated by Django 3.2.6 on 2021-10-08 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_alter_tags_products'),
        ('comment', '0002_auto_20211003_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='content.products', verbose_name='محصولات'),
        ),
    ]