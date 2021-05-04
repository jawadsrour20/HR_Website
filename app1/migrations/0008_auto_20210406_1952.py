# Generated by Django 3.1.7 on 2021-04-06 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20210330_2215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='number_absences',
            new_name='absences_days',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='Employee_department',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='Employee_id',
            new_name='emp_id',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='number_overtime',
            new_name='experience',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='Employee_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='years_of_work',
            new_name='overtime_days',
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
