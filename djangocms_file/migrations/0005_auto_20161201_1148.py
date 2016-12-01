# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_file.models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_file', '0004_set_related_name_for_cmsplugin_ptr'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='show_pdf_preview',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to=djangocms_file.models.UploadPath(b'FilePlugin'), verbose_name='file'),
        ),
    ]
