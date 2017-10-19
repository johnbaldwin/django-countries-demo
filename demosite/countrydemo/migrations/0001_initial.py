# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 19:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CountryInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CountryPageLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('url', models.URLField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='LinkSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100, unique=True)),
                ('host', models.URLField()),
                ('source_url', models.URLField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='countrypagelink',
            name='linkset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='link_set', to='countrydemo.LinkSet'),
        ),
    ]
