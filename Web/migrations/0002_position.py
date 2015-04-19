# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('latitude', models.DecimalField(max_digits=10, decimal_places=5)),
                ('longitude', models.DecimalField(max_digits=10, decimal_places=5)),
                ('place', models.ForeignKey(related_name=b'Place', to='Web.PlaceType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
