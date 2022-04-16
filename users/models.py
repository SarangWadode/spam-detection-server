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
            'exp': current_time + timedelta(minutes=45)
        }
        return encode(data, settings.SECRET_KEY)

    @property
    def as_json(self):
        return { 'username': self.username, 'email': self.email }

    @property
    def unverified_comment_count(self):
        total = 0
        unverified_comments = []
        for comment in self.comment_set.filter(deleted=False):
            orders = self.order_set.filter(product=comment.product).order_by('date_created')
            if orders.count() == 0 or orders[0].date_created > comment.date_posted:
                total += 1
                unverified_comments.append(comment)
        return total, unverified_comments
