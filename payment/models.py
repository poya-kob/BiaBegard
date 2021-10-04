from django.db import models
from django.contrib.auth.models import User

from financial.models import CartItems


class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر مربوطه')

    order_id = models.CharField(max_length=200)
    payment_id = models.CharField(max_length=200)
    amount = models.IntegerField()
    date = models.CharField(default='-', max_length=200)
    card_number = models.CharField(max_length=200, default="****")
    idpay_track_id = models.IntegerField(default=0000)
    bank_track_id = models.TextField(default=0000)
    status = models.IntegerField(default=0)

    cart_items = models.ManyToManyField(CartItems, verbose_name="کارت آیتم ها")

    def __str__(self):
        return self.user.username
