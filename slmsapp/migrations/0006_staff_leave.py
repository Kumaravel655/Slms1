# Generated by Django 4.2 on 2023-05-18 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('slmsapp', '0005_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff_Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_type', models.CharField(max_length=100)),
                ('from_date', models.CharField(max_length=100)),
                ('to_date', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('status', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slmsapp.staff')),
            ],
        ),
    ]