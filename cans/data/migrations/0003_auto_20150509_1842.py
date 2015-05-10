# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20150509_0246'),
    ]

    operations = [
        migrations.AddField(
            model_name='releasegroup',
            name='artist',
            field=models.ForeignKey(default=1, to='data.Artist'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.ImageField(null=True, upload_to=b'artist_images', blank=True),
        ),
    ]
