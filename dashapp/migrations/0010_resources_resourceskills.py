# Generated by Django 3.0.2 on 2021-09-24 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashapp', '0009_projectreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('cecID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('empId', models.IntegerField()),
                ('projectRole', models.CharField(max_length=30)),
                ('phoneNum', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('badge', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'Resources',
            },
        ),
        migrations.CreateModel(
            name='resourceSkills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignedProject', models.CharField(max_length=50)),
                ('technology', models.CharField(max_length=20)),
                ('certiDevnet', models.CharField(max_length=3)),
                ('certiCcna', models.CharField(max_length=3)),
                ('certiCcnp', models.CharField(max_length=3)),
                ('certiSdwan', models.CharField(max_length=3)),
                ('certiSda', models.CharField(max_length=3)),
                ('certiCcie', models.CharField(max_length=3)),
                ('cecId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashapp.Resources')),
            ],
            options={
                'db_table': 'resourceSkills',
            },
        ),
    ]
