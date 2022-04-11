# Generated by Django 3.0.2 on 2020-05-04 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashapp', '0002_dashboard_info_completionzone'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboard_info',
            name='projectStatus',
            field=models.CharField(default='New', max_length=10),
        ),
        migrations.CreateModel(
            name='ProjectDetails',
            fields=[
                ('ProjectId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=3)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('tenure', models.IntegerField()),
                ('numberOfSitesPlanned', models.IntegerField()),
                ('numberOfDevicesMigrated', models.IntegerField()),
                ('totalHoursAllocated', models.IntegerField()),
                ('totalProjectEfforts', models.IntegerField()),
                ('plannedResourceAllocation', models.IntegerField()),
                ('summary', models.TextField()),
                ('completionStatus', models.IntegerField()),
                ('projectName', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dashapp.Dashboard_Info')),
            ],
            options={
                'db_table': 'projectdetails',
            },
        ),
    ]