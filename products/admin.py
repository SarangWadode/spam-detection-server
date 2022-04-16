from dataclasses import fields
from django.contrib import admin

from products.models.product import Product
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    def __str__(self) -> str:
        return self.title


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'sentiment', 'product', 'date_posted', 'user')
    list_display_links = ('pk', 'product', 'user')
    list_filter = ('sentiment', 'product', 'user')
    search_fields = ('text', 'product__name', 'user')
    readonly_fields = ('user', 'product', 'date_posted')
    fieldsets = (
        ('Metadata', {
            'fields': ('user', 'product', 'date_posted')
        }),
        ('Content', {
            'fields': ('text', 'sentiment', 'confidence')
        }),
        ('Deleted', {
            'fields': ('deleted', 'not_spam', 'deletion_reason')
        })
    )

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'product', 'date_created')
    list_display_links = ('pk', 'user', 'product')
    list_filter = ('user', 'product')
    search_fields = ('user', 'product')
    readonly_fields = ('user', 'product', 'date_created')
