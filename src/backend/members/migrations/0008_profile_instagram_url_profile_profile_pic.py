# Generated by Django 4.0.3 on 2022-05-11 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_remove_user_profile_pic_remove_user_user_picture_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='instagram_url',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='image/profile/'),
        ),
    ]
