# Generated by Django 2.1.5 on 2019-03-21 16:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0017_auto_20190321_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 23, 16, 10, 52, 153541, tzinfo=utc)),
        ),
    ]
