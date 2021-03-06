# Generated by Django 3.0.2 on 2020-05-07 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashapp', '0005_auto_20200505_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectdetails',
            name='competativeMigration',
            field=models.CharField(default='No', max_length=10),
        ),
        migrations.AddField(
            model_name='projectdetails',
            name='dealValue',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='projectdetails',
            name='migrationType',
            field=models.CharField(default='Device Migration', max_length=30),
        ),
        migrations.AddField(
            model_name='projectdetails',
            name='numOfDevicesPlannedForMigration',
            field=models.IntegerField(default=3500),
        ),
        migrations.AddField(
            model_name='projectdetails',
            name='numOfSitesMigrated',
            field=models.IntegerField(default=447),
        ),
        migrations.AddField(
            model_name='projectdetails',
            name='numOfWindowsExecutedWidOutRollback',
            field=models.IntegerField(default=448),
        ),
        migrations.AddField(
            model_name='projectdetails',
            name='numberOfAgreedServices',
            field=models.IntegerField(default=451),
        ),
        migrations.AddField(
            model_name='projectdetails',
            name='numberOfServicesUpPostMigration',
            field=models.IntegerField(default=449),
        ),
        migrations.AddField(
            model_name='projectdetails',
            name='numberOfWindowsExecuted',
            field=models.IntegerField(default=448),
        ),
        migrations.AddField(
            model_name='projectdetails',
            name='numberOfWindowsPlanned',
            field=models.IntegerField(default=590),
        ),
        migrations.AddField(
            model_name='projectdetails',
            name='preSales',
            field=models.CharField(default='No', max_length=10),
        ),
        migrations.AddField(
            model_name='projectdetails',
            name='projectDeliveryManager',
            field=models.CharField(default='Prasanna Bakthavatchalam', max_length=50),
        ),
        migrations.AddField(
            model_name='projectdetails',
            name='projectLead',
            field=models.CharField(default='Channabasava', max_length=50),
        ),
        migrations.AddField(
            model_name='projectdetails',
            name='projectManager',
            field=models.CharField(default='Anuj Kumar', max_length=50),
        ),
        migrations.AddField(
            model_name='projectdetails',
            name='region',
            field=models.CharField(default='Americas', max_length=50),
        ),
        migrations.AddField(
            model_name='projectdetails',
            name='repeatBusiness',
            field=models.CharField(default='Yes', max_length=5),
        ),
        migrations.AddField(
            model_name='projectdetails',
            name='segment',
            field=models.CharField(default='GET', max_length=10),
        ),
        migrations.AddField(
            model_name='projectdetails',
            name='theater',
            field=models.CharField(default='Americas', max_length=50),
        ),
        migrations.AddField(
            model_name='projectdetails',
            name='thirdPartyToCisco',
            field=models.CharField(default='Yes', max_length=10),
        ),
        migrations.AlterField(
            model_name='projectdetails',
            name='projectName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashapp.Dashboard_Info'),
        ),
    ]
