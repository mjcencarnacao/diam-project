# Generated by Django 4.0.3 on 2022-05-09 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_remove_comments_ai_probability_feedback_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='Ai_FeedBack',
            new_name='AI_FeedBack',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='Ai_Probability_NegativeFeedBack',
            new_name='AI_Probability_NegativeFeedBack',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='Ai_Probability_PositiveFeedBack',
            new_name='AI_Probability_PositiveFeedBack',
        ),
        migrations.AddField(
            model_name='comments',
            name='critic_feedback',
            field=models.BooleanField(default=False, verbose_name='critic_feedback_about_ai_opinion'),
        ),
    ]
