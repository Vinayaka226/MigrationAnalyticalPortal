# Generated by Django 3.0.2 on 2020-05-05 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashapp', '0004_auto_20200505_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ragdetails',
            name='date',
        ),
        migrations.AddField(
            model_name='ragdetails',
            name='month',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='ragdetails',
            name='year',
            field=models.IntegerField(default=2019),
        ),
    ]
