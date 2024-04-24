# Generated by Django 5.0 on 2024-04-24 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slmsapp', '0019_staff_room_bed_number_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(2, 'staff'), (1, 'admin')], default=1, max_length=50),
        ),
    ]
