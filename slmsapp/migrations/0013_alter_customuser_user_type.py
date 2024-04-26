# Generated by Django 5.0 on 2024-04-25 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slmsapp', '0012_staff_leave_room_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(2, 'staff'), (1, 'admin')], default=1, max_length=50),
        ),
    ]
