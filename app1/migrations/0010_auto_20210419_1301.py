# Generated by Django 3.1.7 on 2021-04-19 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_auto_20210419_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='Number_of_employees',
            field=models.IntegerField(default=0),
        ),
    ]
