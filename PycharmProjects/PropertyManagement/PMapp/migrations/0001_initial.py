# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-20 03:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='building',
            fields=[
                ('building_name', models.IntegerField(primary_key=True, serialize=False)),
                ('building_sdate', models.DateField()),
                ('building_edate', models.DateField()),
                ('building_floor', models.IntegerField()),
                ('building_bcp', models.CharField(max_length=254)),
                ('building_svcp', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='charge',
            fields=[
                ('charge_id', models.IntegerField(primary_key=True, serialize=False)),
                ('charge_name', models.CharField(max_length=254, unique=True)),
                ('charge_count', models.CharField(max_length=254)),
                ('charge_date', models.DateField()),
                ('charge_infor', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='material',
            fields=[
                ('material_id', models.IntegerField(primary_key=True, serialize=False)),
                ('material_nmae', models.CharField(max_length=20, unique=True)),
                ('material_count', models.IntegerField()),
                ('material_price', models.IntegerField()),
                ('material_indate', models.DateField()),
                ('material_state', models.CharField(max_length=20)),
                ('material_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='room',
            fields=[
                ('room_id', models.IntegerField(primary_key=True, serialize=False)),
                ('room_buildingid', models.IntegerField()),
                ('room_ownername', models.CharField(max_length=20, null=True)),
                ('room_indatae', models.DateField(null=True)),
                ('room_s', models.IntegerField()),
                ('room_sort', models.CharField(max_length=1)),
                ('room_type', models.CharField(max_length=10)),
                ('room_property', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('user_id', models.CharField(max_length=18, primary_key=True, serialize=False)),
                ('user_password', models.CharField(max_length=20)),
                ('user_name', models.CharField(max_length=20)),
                ('user_sex', models.CharField(max_length=10)),
                ('user_city', models.CharField(max_length=254)),
                ('user_phonenum', models.CharField(max_length=11, unique=True)),
                ('user_cardnum', models.CharField(max_length=18, unique=True)),
                ('user_type', models.CharField(max_length=20)),
                ('user_roomid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='PMapp.room')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='room_ownerid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='PMapp.user'),
        ),
    ]
