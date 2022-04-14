from django.http.request import HttpRequest
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Comment, Order, Product


def product_list(request: HttpRequest) -> JsonResponse:
    search = request.GET.get('search', '')
    start = request.GET.get('start', 0)
    count = request.GET.get('count', 10)
    return JsonResponse(Product.get_products(search, start, count))

def product_detail(request: HttpRequest, pk: int) -> JsonResponse:
    product = get_object_or_404(Product, pk=pk)
    data = product.as_json
    return JsonResponse( { **data, 'image': request.build_absolute_uri(data['image']) })
