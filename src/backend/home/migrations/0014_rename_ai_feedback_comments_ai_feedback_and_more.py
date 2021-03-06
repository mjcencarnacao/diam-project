# Generated by Django 4.0.3 on 2022-05-07 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_comments_movie_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='Ai_FeedBack',
            new_name='AI_FeedBack',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='Ai_Probability_FeedBack',
        ),
        migrations.AddField(
            model_name='comments',
            name='AI_Probability_NegativeFeedBack',
            field=models.FloatField(null=True, verbose_name='AiNegativeProbability'),
        ),
        migrations.AddField(
            model_name='comments',
            name='AI_Probability_PositiveFeedBack',
            field=models.FloatField(null=True, verbose_name='AiPositiveProbability'),
        ),
    ]
