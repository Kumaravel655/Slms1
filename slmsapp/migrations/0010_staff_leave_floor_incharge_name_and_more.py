# Generated by Django 5.0 on 2024-04-24 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slmsapp', '0009_remove_staff_leave_parent_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_leave',
            name='floor_incharge_name',
            field=models.CharField(default=111, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff_leave',
            name='room_bed_number',
            field=models.CharField(default=1111, max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
