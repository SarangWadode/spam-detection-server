from django.http.request import HttpRequest
from django.http.response import JsonResponse
from users.utils import get_user

def login_required(func):
    def inner(request: HttpRequest, *args, **kwargs):
        bearer = request.headers.get('Authorization')

        # Default authorization
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)

        if bearer is None:
            return JsonResponse({ 'error': 'No auth token found', 'logged_out': True })
        if len(bearer.split()) != 2:
            return JsonResponse({ 'error': 'Invalid token', 'logged_out': True  })

        token = bearer.split()[1]
        try:
            user = get_user(token)
            request.user = user
            return func(request, *args, **kwargs)
        except Exception as e:
            return JsonResponse({ 'error': str(e), 'logged_out': True  })

    return inner
