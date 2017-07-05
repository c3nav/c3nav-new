# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 13:27
from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from django.db import migrations, models
import django.db.models.deletion


def forwards_func(apps, schema_editor):
    ChangeSet = apps.get_model('editor', 'ChangeSet')
    for changeset in ChangeSet.objects.all():
        try:
            changeset.last_update_obj = changeset.updates.latest()
        except ObjectDoesNotExist:
            pass
        try:
            changeset.last_change_obj = changeset.updates.filter(objects_changed=True).latest()
        except ObjectDoesNotExist:
            pass
        changeset.save()

def reverse_func(apps, schema_editor):
    ChangeSet = apps.get_model('editor', 'ChangeSet')
    for changeset in ChangeSet.objects.all():
        try:
            changeset.last_update = changeset.last_update_obj.datetime
        except ObjectDoesNotExist:
            changeset.last_update = changeset.created
        try:
            changeset.last_change = changeset.last_change_obj.datetime
        except ObjectDoesNotExist:
            changeset.last_change = changeset.created
        changeset.save()


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0013_remove_changesetupdate_session_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='changesetupdate',
            options={'get_latest_by': 'datetime', 'ordering': ['datetime', 'pk'], 'verbose_name': 'Change set update',
                     'verbose_name_plural': 'Change set updates'},
        ),
        migrations.AddField(
            model_name='changeset',
            name='last_change_obj',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='editor.ChangeSetUpdate', verbose_name='last object change'),
        ),
        migrations.AddField(
            model_name='changeset',
            name='last_update_obj',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='editor.ChangeSetUpdate', verbose_name='last update'),
        ),
        migrations.RunPython(forwards_func, reverse_func),
        migrations.RemoveField(
            model_name='changeset',
            name='last_change',
        ),
        migrations.RemoveField(
            model_name='changeset',
            name='last_update',
        ),
        migrations.RenameField(
            model_name='changeset',
            old_name='last_change_obj',
            new_name='last_change',
        ),
        migrations.RenameField(
            model_name='changeset',
            old_name='last_update_obj',
            new_name='last_update',
        ),
    ]
