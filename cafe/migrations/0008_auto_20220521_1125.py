# Generated by Django 3.2.7 on 2022-05-21 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0007_auto_20220520_2358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='table_number',
        ),
        migrations.AlterField(
            model_name='table',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]
