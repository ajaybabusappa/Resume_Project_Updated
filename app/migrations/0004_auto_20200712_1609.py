# Generated by Django 3.0.7 on 2020-07-12 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200712_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workexp',
            name='enddate',
        ),
        migrations.RemoveField(
            model_name='workexp',
            name='startdate',
        ),
    ]