# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('user_type', models.CharField(max_length=2, choices=[('a', 'Alumno'), ('d', 'Discipulo'), ('i', 'Instructor'), ('p', 'Profesor'), ('m', 'Maestro'), ('g', 'Gran Maestro')], default='a')),
                ('birthday', models.DateField()),
                ('pic', models.ImageField(blank=True, upload_to='profile_images')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
