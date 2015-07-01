# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('latitude', models.CharField(max_length=64)),
                ('longitude', models.CharField(max_length=64)),
                ('cota', models.IntegerField(null=True)),
                ('bloque', models.CharField(max_length=64, null=True)),
                ('codigo', models.CharField(max_length=32, null=True)),
                ('unidad', models.CharField(max_length=32, null=True)),
                ('tipo', models.CharField(max_length=32, null=True)),
                ('planta', models.IntegerField(null=True)),
                ('descripction', models.CharField(max_length=256, null=True)),
                ('place', models.ForeignKey(related_name='Positions', to='Web.Place')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('url', models.CharField(max_length=512, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='position',
            name='profile',
            field=models.ForeignKey(related_name='Place', to='Web.Profile'),
        ),
    ]
