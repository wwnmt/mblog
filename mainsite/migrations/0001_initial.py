# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
    ]
