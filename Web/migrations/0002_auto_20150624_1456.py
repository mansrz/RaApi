# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='cota',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='position',
            name='descripction',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='facultad',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
