# Generated by Django 3.2.3 on 2021-05-23 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IncidentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('remark', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placeName', models.CharField(max_length=250)),
                ('woreda', models.CharField(max_length=250)),
                ('callerName', models.CharField(max_length=250)),
                ('phoneNumber', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=1000)),
                ('incidentDate', models.DateField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('status', models.CharField(max_length=250)),
                ('incidentType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IncidentManagment.incidenttype')),
            ],
        ),
    ]