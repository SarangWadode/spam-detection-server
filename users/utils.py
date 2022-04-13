from django.contrib.auth import get_user_model
from django.conf import settings
from jwt import decode, exceptions


User = get_user_model()

def get_user(token):
    try:
        data = decode(token, algorithms=['HS256'], key=settings.SECRET_KEY)
        return User.objects.get(pk=data['id'])
    except (exceptions.InvalidSignatureError, exceptions.DecodeError):
        raise TypeError('Invalid token')
    except exceptions.ExpiredSignatureError:
        raise TypeError('Token expired, please login again')
    except Exception:
        raise TypeError('Error authenticating user, please try again')
