# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-14 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0005_bulma'),
    ]

    operations = [
        migrations.CreateModel(
            name='ezdelivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('name', models.CharField(max_length=32, verbose_name='ezdelivery services name')),
                ('env', models.IntegerField(blank=True, choices=[(1, '\u751f\u4ea7\u73af\u5883'), (2, '\u6d4b\u8bd5\u73af\u5883')], null=True, verbose_name='\u8fd0\u884c\u73af\u5883')),
            ],
        ),
        migrations.CreateModel(
            name='featurecollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('name', models.CharField(max_length=32, verbose_name='featurecollection services name')),
                ('env', models.IntegerField(blank=True, choices=[(1, '\u751f\u4ea7\u73af\u5883'), (2, '\u6d4b\u8bd5\u73af\u5883')], null=True, verbose_name='\u8fd0\u884c\u73af\u5883')),
            ],
        ),
        migrations.CreateModel(
            name='homepage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('name', models.CharField(max_length=32, verbose_name='homepage services name')),
                ('env', models.IntegerField(blank=True, choices=[(1, '\u751f\u4ea7\u73af\u5883'), (2, '\u6d4b\u8bd5\u73af\u5883')], null=True, verbose_name='\u8fd0\u884c\u73af\u5883')),
            ],
        ),
        migrations.CreateModel(
            name='popupadmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('name', models.CharField(max_length=32, verbose_name='popupadmin services name')),
                ('env', models.IntegerField(blank=True, choices=[(1, '\u751f\u4ea7\u73af\u5883'), (2, '\u6d4b\u8bd5\u73af\u5883')], null=True, verbose_name='\u8fd0\u884c\u73af\u5883')),
            ],
        ),
        migrations.CreateModel(
            name='voucheradmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('name', models.CharField(max_length=32, verbose_name='voucheradmin services name')),
                ('env', models.IntegerField(blank=True, choices=[(1, '\u751f\u4ea7\u73af\u5883'), (2, '\u6d4b\u8bd5\u73af\u5883')], null=True, verbose_name='\u8fd0\u884c\u73af\u5883')),
            ],
        ),
    ]
