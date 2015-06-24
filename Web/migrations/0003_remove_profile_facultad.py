# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0002_auto_20150624_1456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='facultad',
        ),
    ]
