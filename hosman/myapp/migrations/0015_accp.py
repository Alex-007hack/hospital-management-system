# Generated by Django 5.0.6 on 2024-07-09 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_leave_from_mail'),
    ]

    operations = [
        migrations.CreateModel(
            name='accp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acstatus', models.CharField(max_length=200)),
                ('acreason', models.CharField(max_length=200)),
                ('acdate', models.CharField(max_length=200)),
            ],
        ),
    ]