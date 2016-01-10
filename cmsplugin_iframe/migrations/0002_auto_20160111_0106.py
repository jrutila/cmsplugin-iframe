# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_iframe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iframeplugin',
            name='src',
            field=models.URLField(max_length=1000),
        ),
    ]
