from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from users import urls
from products import urls as product_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(urls)),
    path('', include(product_urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
