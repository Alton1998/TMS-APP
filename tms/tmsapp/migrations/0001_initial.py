# Generated by Django 2.0.4 on 2018-07-08 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='trafficAtA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Trafficdensity', models.FloatField()),
                ('time', models.TimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='trafficAtB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Trafficdensity', models.FloatField()),
                ('time', models.TimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='trafficAtC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Trafficdensity', models.FloatField()),
                ('time', models.TimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='trafficAtD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Trafficdensity', models.FloatField()),
                ('time', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
