# Generated by Django 4.0.3 on 2022-04-14 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='tittle',
        ),
        migrations.AddField(
            model_name='comments',
            name='title',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Title'),
        ),
    ]
