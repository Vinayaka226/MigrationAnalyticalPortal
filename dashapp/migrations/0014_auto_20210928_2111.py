# Generated by Django 3.0.2 on 2021-09-28 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashapp', '0013_automation_enttechnologies_scriptingskills_sptechnologies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resources',
            name='assignedProject',
            field=models.CharField(default='Not Assigned', max_length=50),
        ),
    ]