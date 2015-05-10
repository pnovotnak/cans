# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20150509_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='release_group',
            field=models.ForeignKey(default=1, to='data.ReleaseGroup'),
            preserve_default=False,
        ),
    ]
