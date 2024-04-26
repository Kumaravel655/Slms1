# Generated by Django 5.0 on 2024-04-25 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slmsapp', '0011_staff_timetable_alter_customuser_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff_leave',
            name='id',
        ),
        migrations.AddField(
            model_name='staff_leave',
            name='room_number',
            field=models.CharField(default=1, max_length=50, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(2, 'staff'), (1, 'admin')], default=1, max_length=50),
        ),
    ]
