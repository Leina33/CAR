# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-22 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(null=True, upload_to='')),
                ('brand', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('car_make', models.CharField(max_length=100, null=True)),
                ('price', models.IntegerField(null=True)),
                ('fuel', models.CharField(max_length=20, null=True)),
                ('dimensions', models.CharField(max_length=50, null=True)),
                ('transmission', models.CharField(max_length=100, null=True)),
                ('gears', models.IntegerField(null=True)),
                ('seats', models.IntegerField(null=True)),
                ('power', models.IntegerField(null=True)),
                ('tank_capacity', models.IntegerField(null=True)),
                ('engine_displacement', models.IntegerField(null=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='CarMake',
        ),
    ]
