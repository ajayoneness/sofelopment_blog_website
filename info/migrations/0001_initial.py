# Generated by Django 4.0.3 on 2022-06-09 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=500)),
                ('des', models.TextField(max_length=5000)),
                ('youtube_link', models.URLField(max_length=300)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('comments', models.TextField(max_length=500)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('subscribe', models.EmailField(max_length=250)),
            ],
        ),
    ]