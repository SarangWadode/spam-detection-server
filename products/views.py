from django.http.request import HttpRequest
from django.http.response import JsonResponse
from .models import Comment, Order, Product


def product_list(request: HttpRequest) -> JsonResponse:
    search = request.GET.get('search', '')
    start = request.GET.get('start', 0)
    count = request.GET.get('count', 10)
    return JsonResponse(Product.get_products(search, start, count))
