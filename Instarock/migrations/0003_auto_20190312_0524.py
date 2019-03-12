# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-12 02:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('Instarock', '0002_auto_20190312_0158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comm', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_following', to='Instarock.User')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_followers', to='Instarock.User')),
            ],
        ),
        migrations.CreateModel(
            name='idss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', pyuploadcare.dj.models.ImageField(blank=True)),
                ('name', models.CharField(blank=True, max_length=31)),
                ('caption', models.CharField(blank=True, max_length=50)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('likes', models.ManyToManyField(blank=True, related_name='likes', to='Instarock.User')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='Instarock.User')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', pyuploadcare.dj.models.ImageField(blank=True)),
                ('bio', models.CharField(default='Hi!', max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='Instarock.User')),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Instarock.Image'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Instarock.User'),
        ),
    ]
