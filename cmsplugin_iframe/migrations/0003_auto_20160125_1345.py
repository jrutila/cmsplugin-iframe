# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_iframe', '0002_auto_20160111_0106'),
    ]

    operations = [
        migrations.AddField(
            model_name='iframeplugin',
            name='height',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='iframeplugin',
            name='width',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
