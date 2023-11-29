# Generated by Django 4.2.6 on 2023-11-23 19:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='create_date',
        ),
        migrations.AddField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 23, 19, 3, 27, 623853, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2023, 11, 23, 19, 3, 27, 624211, tzinfo=datetime.timezone.utc)),
        ),
    ]