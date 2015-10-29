# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chirp', '0002_auto_20151029_1122'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chirp',
            options={'ordering': ['-added']},
        ),
    ]
