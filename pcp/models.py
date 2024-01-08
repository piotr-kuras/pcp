from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Product(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=200)
    product = models.ForeignKey(to='Product', on_delete=models.CASCADE)
    product_url = models.URLField()

    def __str__(self):
        return self.name


class Price(models.Model):
    shop = models.ForeignKey(to='Shop', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.shop.product.name} - {self.shop.name} - {self.price} - {self.date}"


@receiver(post_save, sender=Product)
def product_handler(sender, **kwargs):
    from pcp.tasks import refresh_products_prices
    refresh_products_prices.delay()
