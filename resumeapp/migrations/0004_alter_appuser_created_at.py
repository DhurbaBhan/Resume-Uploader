# Generated by Django 4.0.4 on 2022-10-30 08:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0003_alter_appuser_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 30, 14, 35, 45, 248851)),
        ),
    ]
