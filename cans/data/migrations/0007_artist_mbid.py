# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_auto_20150509_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='mbid',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
