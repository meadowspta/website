# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-28 17:18
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asset', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, help_text=b'A slug will be genereated if left blank.', max_length=255)),
                ('publish_date', models.DateTimeField(default=datetime.datetime.now)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True, verbose_name=b'Publish')),
                ('body', models.TextField()),
                ('content_images', models.ManyToManyField(blank=True, related_name='content_images', to='asset.File')),
                ('main_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.File')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=b'Author')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
