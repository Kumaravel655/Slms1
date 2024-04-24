# Generated by Django 5.0 on 2024-04-24 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slmsapp', '0013_alter_customuser_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='room_bed_number',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'admin'), (2, 'staff')], default=1, max_length=50),
        ),
    ]