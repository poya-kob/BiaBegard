from django.db import models


class ProductsManager(models.Manager):

    def get_active_product(self):
        return self.get_queryset().filter(active=True)

    def get_products_by_category(self, category_name):
        return self.get_queryset().filter(category__name__iexact=category_name, active=True)
