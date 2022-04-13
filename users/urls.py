from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('login', views.login_user, name='login'),
    path('register', views.register, name='register'),
]
