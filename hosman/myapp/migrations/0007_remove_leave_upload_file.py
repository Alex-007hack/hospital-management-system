# Generated by Django 5.0.1 on 2024-06-24 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_leave'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leave',
            name='upload_file',
        ),
    ]