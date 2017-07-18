# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-18 13:42
from __future__ import unicode_literals

from django.db import migrations
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_forms', '0005_formfield_field_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formdefinition',
            name='description',
            field=djangocms_text_ckeditor.fields.HTMLField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='help_text',
            field=djangocms_text_ckeditor.fields.HTMLField(blank=True, help_text='A description / instructions for this field.', verbose_name='Description'),
        ),
    ]
