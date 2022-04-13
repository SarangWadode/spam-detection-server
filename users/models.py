from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import datetime, timedelta, timezone
from jwt import encode


class CustomUser(AbstractUser):
    @property
    def token(self) -> str:
        return self.__get_token()

    def __get_token(self):
        current_time = datetime.now(tz=timezone.utc)
        data = {
            'id': self.pk,
            'iat': current_time,
            'exp': current_time + timedelta(minutes=15)
        }
        return encode(data, settings.SECRET_KEY)

    @property
    def as_json(self):
        return { 'username': self.username, 'email': self.email }
