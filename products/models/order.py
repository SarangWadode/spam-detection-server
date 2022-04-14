import imp
from itertools import count
from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import get_list_or_404
from products.utils import create_json
from .product import Product


User = get_user_model()

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [ models.Index(fields=['product', 'user']) ]
        ordering = ['-date_created']
    
    @property
    def as_json(self):
        return {
            'date': self.date_created,
        }

    @classmethod
    def get_orders(cls, user, start=0, count=10):
        start, count = int(start), int(count)
        orders = cls.objects.filter(user=user)[start:start+count].values()
        return create_json(orders, start)
