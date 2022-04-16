from django.contrib.auth import get_user_model
from django.db import models
from products.utils import create_json


User = get_user_model()

class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name='Product Title')
    description = models.TextField()
    image = models.ImageField(verbose_name='Product image')

    def __str__(self) -> str:
        return self.name

    @property
    def as_json(self):
        comments = self.comment_set.get_queryset()\
            .filter(deleted=False, not_spam=False)\
            .select_related()[0:5]\
            .values('user__username', 'text', 'sentiment', 'confidence', 'date_posted')
        return {
            'title': self.name,
            'description': self.description,
            'pk': self.pk,
            'image': self.image.url,
            'comments': list(comments)
        }

    @classmethod
    def get_products(cls, query='', start=0, count=10):
        start = int(start)
        count = int(count)
        result_query = models.Q(name__icontains=query) | models.Q(description__icontains=query)
        filtered_products = cls.objects.filter(result_query)[start:start + count].values('name', 'image', 'pk')
        return create_json(filtered_products, start)
