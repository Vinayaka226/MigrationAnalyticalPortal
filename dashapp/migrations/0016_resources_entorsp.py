# Generated by Django 3.0.2 on 2021-09-29 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashapp', '0015_remove_resourceskills_technology'),
    ]

    operations = [
        migrations.AddField(
            model_name='resources',
            name='entOrSp',
            field=models.CharField(default='ENT', max_length=50),
        ),
    ]