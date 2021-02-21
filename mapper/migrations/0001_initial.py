# Generated by Django 3.1.6 on 2021-02-21 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeoData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('continent_code', models.CharField(max_length=5)),
                ('continent_name', models.CharField(max_length=50)),
                ('country_code', models.CharField(max_length=10)),
                ('country_name', models.CharField(max_length=50)),
                ('region_code', models.CharField(max_length=5)),
                ('region_name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=50)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='IpAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(protocol='IPv4')),
                ('geo_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ip_adresses', to='mapper.geodata')),
            ],
        ),
    ]
