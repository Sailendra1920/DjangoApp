# Generated by Django 5.0.7 on 2024-07-30 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_username_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='username',
            name='dob',
        ),
    ]
