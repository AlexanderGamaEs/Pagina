# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150616_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionMainPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=48)),
                ('content', models.TextField()),
                ('last_edition', models.DateField()),
            ],
        ),
    ]
