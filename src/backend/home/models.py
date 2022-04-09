from email.mime import image
from django.db import models

# Create your models here.


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    raw = models.JSONField()
    entry = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
