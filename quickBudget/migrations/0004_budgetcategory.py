# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickBudget', '0003_auto_20170220_0057'),
    ]

    operations = [
        migrations.CreateModel(
            name='BudgetCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]