# Generated by Django 4.0.3 on 2022-05-12 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0009_remove_profile_profile_pic_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default-user-image.png', null=True, upload_to='image/profile/'),
        ),
    ]