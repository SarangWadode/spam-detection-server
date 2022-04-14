from django.db import models
from django.contrib.auth import get_user_model
from .product import Product


User = get_user_model()

class Order(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        indexes = [ models.Index(fields=['product_id', 'user_id']) ]
        ordering = ['-date_created']
