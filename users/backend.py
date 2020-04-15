from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend as _ModelBackend

class EmailOrUsernameModelBackend(_ModelBackend):
    def authenticate(self, username=None, password=None):
        # if '@' in username:
        #     kwargs = {'email': username}
        # else:
        #     kwargs = {'username': username}
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None