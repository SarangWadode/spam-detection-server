from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from jwt import encode


class CustomUser(AbstractUser):
    @property
    def token(self) -> str:
        return self.__get_token()

    def __get_token(self):
        data = { 'id': self.pk }
        return encode(data, settings.SECRET_KEY)

    @property
    def as_json(self):
        return { 'username': self.username, 'email': self.email }
