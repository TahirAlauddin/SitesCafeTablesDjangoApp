# Generated by Django 4.0.4 on 2022-05-22 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0002_alter_table_guid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='guid',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
