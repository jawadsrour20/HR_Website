# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2020-03-16 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20200316_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_taken',
            name='Number_of_credits',
            field=models.IntegerField(),
        ),
    ]
