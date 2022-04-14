from django.contrib.auth import get_user_model
from products.utils import create_json
from django.db import models
from .product import Product


User = get_user_model()

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sentiment = models.CharField(verbose_name='predicted sentiment', blank=True, null=True, max_length=15)
    confidence = models.FloatField(verbose_name='Confidence of predicted sentiment', blank=True, null=True)
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
    deletion_reason = models.TextField(blank=True, null=True)
    not_spam = models.BooleanField(default=False)

    class Meta:
        indexes = [ models.Index(fields=['product', 'user']) ]
        ordering = ['-date_posted']

    @classmethod
    def get_comments(cls, product:Product, start=0, count=10):
        count, start = int(count), int(start)
        comments = cls.objects.filter(product=product, deleted=False, not_spam=False)[start:start+count]\
            .values('user__username', 'text', 'sentiment', 'confidence', 'date_posted')
        return create_json(comments, start)
