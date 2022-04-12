from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_regular_user = models.BooleanField('Is Regular', default=False)
    is_premium_user = models.BooleanField('Is Premium', default=False)
    is_pro_user = models.BooleanField('Is Pro', default=False)

# Create your models here.
