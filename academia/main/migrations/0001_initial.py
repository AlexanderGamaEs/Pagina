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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(max_length=2, default='a', choices=[('a', 'Alumno'), ('d', 'Discipulo'), ('i', 'Instructor'), ('p', 'Profesor'), ('m', 'Maestro'), ('g', 'Gran Maestro')])),
                ('birthday', models.DateField()),
                ('pic', models.ImageField(upload_to='profile_images', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
