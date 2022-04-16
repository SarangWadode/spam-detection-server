from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('products', views.product_list, name='product_list'),
    path('products/<int:pk>', views.product_detail, name='product_detail'),
    path('products/<int:pk>/buy', views.buy_product, name='product_buy'),
    path('products/<int:pk>/comment', views.add_comment, name='add_comment'),
    path('products/<int:pk>/comments', views.comments, name='comment_list'),
    path('orders', views.order_list, name='orders'),
    path('products/create', views.add_product, name='add_product')
]
