# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 10:14
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
                ('name', models.CharField(db_index=True, max_length=200)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('created_by', models.CharField(db_index=True, max_length=200)),
                ('updated_at', models.DateField(auto_now=True)),
                ('updated_by', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant_Name', models.CharField(blank=True, db_index=True, max_length=200)),
                ('launch_Date', models.DateField(blank=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('created_by', models.CharField(db_index=True, max_length=200)),
                ('updated_at', models.DateField(auto_now=True)),
                ('updated_by', models.CharField(max_length=10)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='catalogue.Brand')),
            ],
        ),
        migrations.CreateModel(
            name='Kit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('created_by', models.CharField(db_index=True, max_length=200)),
                ('updated_at', models.DateField(auto_now=True)),
                ('updated_by', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='KitCarRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('created_by', models.CharField(db_index=True, max_length=200)),
                ('updated_at', models.DateField(auto_now=True)),
                ('updated_by', models.CharField(max_length=10)),
                ('carid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='catalogue.Car')),
                ('kitid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='catalogue.Kit')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('created_by', models.CharField(db_index=True, max_length=200)),
                ('updated_at', models.DateField(auto_now=True)),
                ('updated_by', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='brand',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='catalogue.Manufacturer'),
        ),
    ]
