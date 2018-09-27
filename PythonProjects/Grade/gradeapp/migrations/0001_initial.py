# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-05 07:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='grade',
            fields=[
                ('grade_id', models.IntegerField(primary_key=True, serialize=False)),
                ('grade_name', models.CharField(max_length=20)),
                ('grade_size', models.IntegerField()),
                ('grade_money', models.FloatField()),
                ('grade_img', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('stu_id', models.IntegerField(primary_key=True, serialize=False)),
                ('stu_name', models.CharField(max_length=20, unique=True)),
                ('stu_grade_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gradeapp.grade')),
            ],
        ),
    ]
