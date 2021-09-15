from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Products, PricesHistory


@receiver(post_save, sender=Products)
def create_price_history(sender, instance: Products, created, **kwargs):
    if instance.off_price != instance.original_off_price > 0:
        PricesHistory.objects.create(product=instance, product_price=instance.off_price)
    elif instance.product_price != instance.original_price:
        PricesHistory.objects.create(product=instance, product_price=instance.product_price)
