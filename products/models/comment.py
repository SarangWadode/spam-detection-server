from django.contrib.auth import get_user_model
from django.db import models
from products.utils import create_json
from .product import Product


User = get_user_model()

class Comment(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    sentiment = models.CharField(verbose_name='predicted sentiment', blank=True, null=True, max_length=15)
    confidence = models.FloatField(verbose_name='Confidence of predicted sentiment', blank=True, null=True)
    text = models.TextField()
    date_posted = models.DateField(auto_now_add=True)

    class Meta:
        indexes = [ models.Index(fields=['product_id', 'user_id']) ]
