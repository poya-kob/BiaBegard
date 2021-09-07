import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# from financial.models import Orders


class Post(models.Model):
    type_of_shipping = [
        ('post', 'post'),
        ('pishtaz', 'pishtaz'),
        ('aadi', 'aadi'),
        ('ersal_forooshgahi', "ersal_forooshgahi"),
        ('ersal_pekmotori', 'ersal_peykmotori '),

    ]

    date_chices = [
        (datetime.date)
    ]

    day_division = [
        ('صبح', '۸ تا ۱۲ بعد از ظهر'),
        ('ظهر', '۱۲ تا ۶ عصر'),
        ("شب", "۶ عصر تا ۱۲ شب"),
    ]

    post = models.CharField(max_length=20, choices=type_of_shipping)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_recived = models.CharField(max_length=3, choices=day_division)
    date_recived = models.DateField()
