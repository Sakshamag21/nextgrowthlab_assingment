# Generated by Django 4.1.2 on 2024-10-14 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('manager', 'Manager'), ('employee', 'Employee')], default='employee', max_length=10),
        ),
    ]
