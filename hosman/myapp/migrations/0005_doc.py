# Generated by Django 5.0.1 on 2024-06-23 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='doc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=25)),
                ('dpassword', models.CharField(max_length=25)),
                ('demail', models.CharField(max_length=25)),
            ],
        ),
    ]