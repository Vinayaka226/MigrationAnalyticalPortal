# Generated by Django 3.0.2 on 2021-10-05 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashapp', '0019_issue_lessons_project_names'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessons',
            name='modelNumber',
            field=models.CharField(default='NA', max_length=15),
        ),
    ]
