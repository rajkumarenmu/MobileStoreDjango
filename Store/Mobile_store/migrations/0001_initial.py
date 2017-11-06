# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-21 14:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mobiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_no', models.CharField(max_length=10)),
                ('description', models.TextField(max_length=100)),
                ('price', models.FloatField(max_length=10)),
                ('weight', models.FloatField(max_length=10)),
                ('ram', models.FloatField(max_length=10)),
                ('internal_memory', models.FloatField(max_length=10)),
                ('front_camera', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='uploads')),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mobile_store.Brand')),
            ],
        ),
    ]
