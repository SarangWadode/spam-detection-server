import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import users


@csrf_exempt
def login(request):
    data = json.loads(request.body)
    email = data.get('email', None)
    password = data.get('password', None)
    if email is None or password is None:
        return JsonResponse({'error': 'Missing email or password'})
    user = authenticate(email=email, password=password)
    print(email,password,user)
    if user is not None:
        login(request, user)
        return JsonResponse({"message": "You are logged in."})
    return JsonResponse({"message": "Invalid credentials."})

@csrf_exempt
def register(request):
    data = json.loads(request.body)
    email = data.get('email', None)
    username = data.get('username', None)
    password = data.get('password', None)
    if email is None or password is None or username is None:
        return JsonResponse({'error': 'Missing email or password'})
    user = User.objects.create_user(username=username, email=email, password=password)
    user.save()
    return JsonResponse({"message": "You are registered."})
