from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_since = models.DateTimeField(auto_now_add=True)
    is_regular_user = models.BooleanField('Is Regular', default=True)
    is_premium_user = models.BooleanField('Is Premium', default=False)
    is_pro_user = models.BooleanField('Is Pro', default=False)
