from email.mime import image
from django.db import models

# Create your models here.


class Movie(models.Model):

    raw = models.JSONField()
    name = models.CharField('Movie Name', max_length=120, blank=True, null=True)
    entry = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title



