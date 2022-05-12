from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_since = models.DateTimeField(auto_now_add=True)
    is_regular_user = models.BooleanField('Is Regular', default=True)
    is_premium_user = models.BooleanField('Is Premium', default=False)
    is_pro_user = models.BooleanField('Is Pro', default=False)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="image/profile/")


##APAGAR
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    instagram_url= models.CharField(max_length=225,null=True,blank=True)

    def __str__(self):
        return str(self.user)
