from django.db import models
from django.db.models import Q


class ProductsManager(models.Manager):

    def get_active_product(self):
        return self.get_queryset().filter(active=True)

    def get_products_by_category(self, category_name):
        return self.get_queryset().filter(category__name__iexact=category_name, active=True)

    def search(self, query):
        lookup = (
                Q(name__icontains=query) |
                Q(short_description__icontains=query) |
                Q(full_description__icontains=query) |
                Q(tag__title__icontains=query)
        )
        return self.get_queryset().filter(lookup, active=True).distinct()
