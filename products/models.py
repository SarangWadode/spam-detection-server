from django.contrib.auth import get_user_model
from django.db import models
from .utils import create_json


User = get_user_model()

class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name='Product Title')
    description = models.TextField()
    image = models.ImageField(verbose_name='Product image', upload_to='uploads')

    def __str__(self) -> str:
        return f'''
            {self.name.center(50)}
        Image: {self.image}
        {self.description}
        '''

    @classmethod
    def get_products(cls, query='', start=0, count=10):
        result_query = models.Q(name__icontains=query) | models.Q(description__icontains=query)
        filtered_products = cls.objects.filter(result_query)[start:start + count].values()
        return create_json(filtered_products, start)


class Comment(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    sentiment = models.CharField(verbose_name='predicted sentiment', blank=True, null=True, max_length=15)
    confidence = models.FloatField(verbose_name='Confidence of predicted sentiment', blank=True, null=True)
    text = models.TextField()
    date_posted = models.DateField(auto_now_add=True)

    class Meta:
        indexes = [ models.Index(fields=['product_id', 'user_id']) ]


class Order(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        indexes = [ models.Index(fields=['product_id', 'user_id']) ]
        ordering = ['-date_created']
