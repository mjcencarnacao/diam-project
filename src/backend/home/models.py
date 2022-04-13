from email.mime import image
from django.db import models
from members.models import User

# Create your models here.


class Movie(models.Model):
    raw = models.JSONField()
    name = models.CharField('Movie Name', max_length=120, blank=True, null=True)
    entry = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name.__str__()


class Comments(models.Model):
    title = models.CharField('Title', max_length=500, blank=True, null=True)
    comment = models.TextField('Comment', blank=True, null= True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    critic = models.ForeignKey(User, on_delete=models.CASCADE)
    entry = models.DateTimeField(auto_now_add=True)


