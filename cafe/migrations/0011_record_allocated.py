# Generated by Django 3.2.7 on 2022-05-21 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0010_auto_20220521_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='allocated',
            field=models.BooleanField(default=False),
        ),
    ]
