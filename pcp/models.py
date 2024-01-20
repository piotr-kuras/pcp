from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.conf import settings
from django.utils import timezone


class Product(models.Model):
    ALLOWED_DOMAINS = ['ceneo.pl']
    name = models.CharField(max_length=200)
    url = models.URLField()
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        if not self.added_by:
            self.added_by = self.request.user
        super().save(*args, **kwargs)


class Shop(models.Model):
    name = models.CharField(max_length=200)
    product = models.ForeignKey(to='Product', on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return self.name

    def get_url(self):
        return Price.objects.filter(shop=self).order_by('price').first().product_url

    def get_price(self):
        today_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        today_end = today_start + timezone.timedelta(days=1)
        price = Price.objects.filter(
            shop=self,
            date__range=(today_start, today_end)
        ).order_by('price').first()

        return str(price.price) if price else 'brak ceny'


class Price(models.Model):
    shop = models.ForeignKey(to='Shop', on_delete=models.CASCADE)
    product_url = models.URLField(max_length=750)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.shop.product.name} - {self.shop.name} - {self.price} - {self.date}"

    def save(self, *args, **kwargs):
        if not self.date:
            self.date = timezone.now()
        super().save(*args, **kwargs)


@receiver(post_save, sender=Product)
def product_handler(sender, **kwargs):
    from pcp.tasks import refresh_products_prices
    refresh_products_prices.delay()
