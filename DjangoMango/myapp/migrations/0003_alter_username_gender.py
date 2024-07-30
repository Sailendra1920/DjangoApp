# Generated by Django 5.0.7 on 2024-07-30 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_username_dob_alter_username_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='username',
            name='gender',
            field=models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=2, verbose_name='Gender'),
        ),
    ]
