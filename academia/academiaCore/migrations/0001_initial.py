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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('user_type', models.CharField(choices=[('a', 'Alumno'), ('d', 'Discipulo'), ('i', 'Instructor'), ('p', 'Profesor'), ('m', 'Maestro'), ('g', 'Gran Maestro')], default='a', max_length=2)),
                ('birthday', models.DateField()),
                ('pic', models.ImageField(blank=True, upload_to='profile_images')),
                ('enable', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
