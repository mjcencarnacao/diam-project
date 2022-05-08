# Generated by Django 4.0.3 on 2022-05-07 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_remove_comments_ai_feedback_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='Ai_Probability_FeedBack',
        ),
        migrations.AddField(
            model_name='comments',
            name='Ai_Probability_NegativeFeedBack',
            field=models.FloatField(null=True, verbose_name='NegativeProbabilityAI'),
        ),
        migrations.AddField(
            model_name='comments',
            name='Ai_Probability_PositiveFeedBack',
            field=models.FloatField(null=True, verbose_name='PositiveProbabilityAi'),
        ),
    ]