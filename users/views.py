from django.contrib.auth import authenticate, get_user_model, login
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads

User = get_user_model()

@csrf_exempt
def login_user(request):
    data = loads(request.body)
    username = data.get('username', None)
    password = data.get('password', None)

    if username is None or password is None:
        return JsonResponse({ 'error': 'Missing email or password' })

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return JsonResponse({ 'message': 'You are logged in.', 'token': user.token, 'user': user.as_json })
    return JsonResponse({ 'error': 'Invalid credentials.' })

@csrf_exempt
def register(request):
    data = loads(request.body)
    email = data.get('email', None)
    username = data.get('username', None)
    password = data.get('password', None)
    if email is None or password is None or username is None:
        return JsonResponse({ 'error': 'Missing email or password' })

    if User.objects.filter(username=username).exists():
        return JsonResponse({ 'error': f'"{username}" already exists' })

    user = User.objects.create_user(username=username, email=email, password=password)
    user.save()
    return JsonResponse({ 'message': 'You are registered.' })
