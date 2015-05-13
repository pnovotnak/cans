# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_queue'),
    ]

    operations = [
        migrations.AddField(
            model_name='releasegroup',
            name='image',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
