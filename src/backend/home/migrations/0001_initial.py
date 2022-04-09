# Generated by Django 4.0.3 on 2022-04-03 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieListEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('year', models.IntegerField()),
                ('rating', models.FloatField()),
                ('image', models.ImageField(upload_to='')),
                ('url', models.SlugField()),
                ('entry', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
