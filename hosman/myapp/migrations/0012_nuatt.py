# Generated by Django 5.0.1 on 2024-06-27 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_nusleave'),
    ]

    operations = [
        migrations.CreateModel(
            name='nuatt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drname', models.CharField(max_length=200)),
                ('drmail', models.CharField(max_length=200)),
                ('drdate', models.CharField(max_length=200)),
                ('drstatus', models.CharField(max_length=200)),
                ('drcomment', models.CharField(max_length=200)),
            ],
        ),
    ]
