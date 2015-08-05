# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0003_auto_20150720_2238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('codmat', models.CharField(max_length=64)),
                ('hora_inicio', models.CharField(max_length=64)),
                ('hora_fin', models.CharField(max_length=64)),
                ('dia', models.CharField(max_length=64)),
                ('aula', models.CharField(max_length=64)),
                ('bloque', models.CharField(max_length=64)),
                ('campus', models.CharField(max_length=64)),
                ('bloquecampus', models.CharField(max_length=64)),
                ('position', models.ForeignKey(related_name='schedules', to='Web.Position', null=True)),
            ],
        ),
    ]
