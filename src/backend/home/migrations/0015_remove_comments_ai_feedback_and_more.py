# Generated by Django 4.0.3 on 2022-05-07 14:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0014_rename_ai_feedback_comments_ai_feedback_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='AI_FeedBack',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='AI_Probability_NegativeFeedBack',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='AI_Probability_PositiveFeedBack',
        ),
        migrations.AddField(
            model_name='comments',
            name='Ai_FeedBack',
            field=models.IntegerField(null=True, verbose_name='AiFeedBack'),
        ),
        migrations.AddField(
            model_name='comments',
            name='Ai_Probability_FeedBack',
            field=models.FloatField(null=True, verbose_name='AiProbabilityFeedBack'),
        ),
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('have_seen', models.BooleanField(default=False)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserLikeMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentsLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.comments')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
