# Generated by Django 3.1.7 on 2021-03-30 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20210330_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
