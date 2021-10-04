# Generated by Django 3.2.6 on 2021-09-21 05:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content', '0009_alter_tags_products'),
        ('financial', '0003_auto_20210914_1048'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField(default=1, verbose_name='تعداد از محصول')),
                ('status', models.CharField(choices=[('paid', 'پرداخت شده'), ('pending', 'منتظر پرداخت')], default='pending', max_length=7, verbose_name='وضعیت پرداخت')),
            ],
        ),
        migrations.CreateModel(
            name='Carts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد کارت')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='زمان اخرین تغییرات')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر مربوطه')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=200)),
                ('payment_id', models.CharField(max_length=200)),
                ('amount', models.IntegerField()),
                ('date', models.CharField(default='-', max_length=200)),
                ('card_number', models.CharField(default='****', max_length=200)),
                ('idpay_track_id', models.IntegerField(default=0)),
                ('bank_track_id', models.TextField(default=0)),
                ('status', models.IntegerField(default=0)),
                ('cart_items', models.ManyToManyField(to='financial.CartItems', verbose_name='کارت آیتم ها')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر مربوطه')),
            ],
        ),
        migrations.RemoveField(
            model_name='orders',
            name='offs',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='shipping',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='user',
        ),
        migrations.DeleteModel(
            name='OrderDetails',
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
        migrations.AddField(
            model_name='cartitems',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='financial.carts', verbose_name='کارت مربوطه'),
        ),
        migrations.AddField(
            model_name='cartitems',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.products', verbose_name='محصول مربوطه'),
        ),
    ]
