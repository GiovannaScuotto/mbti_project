from django.contrib.auth.backends import ModelBackend
from .models import USERS

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = USERS.objects.get(nick=username)
            if user.pwd == password:
                return user
        except USERS.DoesNotExist:
            return None
        #return None