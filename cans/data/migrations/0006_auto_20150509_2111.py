# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_track'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='track',
            options={'ordering': ('-number', 'name')},
        ),
        migrations.AddField(
            model_name='track',
            name='length',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='track',
            name='number',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
