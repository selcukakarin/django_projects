# Generated by Django 3.2.3 on 2021-05-22 16:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 22, 16, 23, 21, 236467, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
