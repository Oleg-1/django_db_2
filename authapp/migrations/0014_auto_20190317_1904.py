# Generated by Django 2.1.5 on 2019-03-17 16:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0013_auto_20190317_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 19, 16, 4, 39, 387614, tzinfo=utc)),
        ),
    ]