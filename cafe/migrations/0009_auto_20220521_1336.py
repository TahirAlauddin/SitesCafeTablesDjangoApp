# Generated by Django 3.2.7 on 2022-05-21 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0008_auto_20220521_1125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='tables',
        ),
        migrations.AddField(
            model_name='record',
            name='tables',
            field=models.ManyToManyField(to='cafe.Table'),
        ),
    ]
