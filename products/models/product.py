from django.contrib.auth import get_user_model
from django.db import models
from products.utils import create_json


User = get_user_model()

class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name='Product Title')
    description = models.TextField()
    image = models.ImageField(verbose_name='Product image')

    def __str__(self) -> str:
        return f'''
            {self.name.center(50)}
        Image: {self.image}
        {self.description}
        '''

    @property
    def as_json(self):
        return { 
            'title': self.name,
            'description': self.description,
            'pk': self.pk,
            'image': self.image.url
        }

    @classmethod
    def get_products(cls, query='', start=0, count=10):
        result_query = models.Q(name__icontains=query) | models.Q(description__icontains=query)
        filtered_products = cls.objects.filter(result_query)[start:start + count].values('name', 'image', 'pk')
        return create_json(filtered_products, start)
