# -*- coding: utf-8 -*-

# Generated by Django 3.2.10 on 2022-02-10 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0013_auto_20220210_0525'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leaguegameplayer',
            old_name='player',
            new_name='assigned_player',
        ),
    ]
