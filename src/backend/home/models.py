from email.mime import image

from django.conf import settings
from django.db import models
from members.models import User


# Create your models here.


class Movie(models.Model):
    raw = models.JSONField()
    name = models.CharField('Movie Name', max_length=120, blank=True, null=True)
    entry = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name.__str__()


class Comments(models.Model):
    title = models.CharField('Title', max_length=500, blank=True, null=True)
    comment = models.TextField('Comment', blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    movie_name = models.CharField('Movie_Name', max_length=500, blank=True, null=True)
    critic = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    critic_username = models.CharField('Critic_Name', max_length=500, blank=True, null=True)
    entry = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    AI_FeedBack = models.IntegerField("AiFeedBack", null=True)
    AI_Probability_PositiveFeedBack = models.FloatField("PositiveProbabilityAi", null=True)
    AI_Probability_NegativeFeedBack = models.FloatField("NegativeProbabilityAI", null=True)
    critic_feedback = models.BooleanField("critic_feedback_about_ai_opinion", default=False)


class WatchList(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    have_seen = models.BooleanField(default=False)


class CommentsLikes(models.Model):
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)


class UserLikeMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
