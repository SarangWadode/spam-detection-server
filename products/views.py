from json import loads
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .decorators import login_required
from .models import Comment, Order, Product


def product_list(request: HttpRequest) -> JsonResponse:
    search = request.GET.get('search', '')
    start = request.GET.get('start', 0)
    count = request.GET.get('count', 10)
    return JsonResponse({ 
        'base_url': request.build_absolute_uri(settings.MEDIA_URL),
        **Product.get_products(search, start, count)
    })

def product_detail(request: HttpRequest, pk: int) -> JsonResponse:
    product = get_object_or_404(Product, pk=pk)
    data = product.as_json
    return JsonResponse( { **data, 'image': request.build_absolute_uri(data['image']) })

@csrf_exempt
@login_required
def buy_product(request: HttpRequest, pk: int) -> JsonResponse:
    product = get_object_or_404(Product, pk=pk)
    try:
        order = Order.objects.create(user=request.user, product=product)
        order.save()
        return JsonResponse({ 'success': 'Order successful' })
    except:
        return JsonResponse({ 'error': 'Error purchasing product' })

@login_required
def order_list(request: HttpRequest) -> JsonResponse:
    start = request.GET.get('start', 0)
    count = request.GET.get('count', 10)
    return JsonResponse(Order.get_orders(request.user, start, count))

@csrf_exempt
@login_required
def add_comment(request: HttpRequest, pk: int) -> JsonResponse:
    product = get_object_or_404(Product, pk=pk)
    text = loads(request.body).get('text')

    if text is None:
        return JsonResponse({ 'error': 'Comment text is required' })
    
    comment = Comment.objects.create(text=text, user=request.user, product=product)
    comment.save()
    return JsonResponse({ 'success': 'Comment added successfully' })

def comments(request: HttpRequest, pk: int) -> JsonResponse:
    product = get_object_or_404(Product, pk=pk)
    count = request.GET.get('count', 10)
    start = request.GET.get('start', 0)
    return JsonResponse(Comment.get_comments(product, start, count))
