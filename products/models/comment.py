from django.contrib.auth import get_user_model
from django.db import models
from products.utils import create_json
from .product import Product


User = get_user_model()

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sentiment = models.CharField(verbose_name='predicted sentiment', blank=True, null=True, max_length=15)
    confidence = models.FloatField(verbose_name='Confidence of predicted sentiment', blank=True, null=True)
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [ models.Index(fields=['product', 'user']) ]
        ordering = ['-date_posted']

    @classmethod
    def get_comments(cls, product:Product, start=0, count=10):
        count, start = int(count), int(start)
        comments = cls.objects.filter(product=product)[start:start+count]\
            .values('user__username', 'text', 'sentiment', 'confidence', 'date_posted')
        return create_json(comments, start)
