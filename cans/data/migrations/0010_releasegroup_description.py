# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_releasegroup_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='releasegroup',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
    ]
