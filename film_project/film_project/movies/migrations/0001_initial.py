# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('country', models.CharField(max_length=30)),
                ('release_date_world', models.DateField()),
                ('release_date_uzb', models.DateField()),
                ('description', models.TextField(max_length=400)),
                ('IMDB', models.FloatField()),
                ('rating', models.FloatField()),
                ('age_restriction', models.IntegerField()),
                ('duration', models.TimeField()),
            ],
        ),
    ]
