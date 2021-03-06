# Generated by Django 2.2.8 on 2019-12-24 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mapdata', '0078_reports'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'default_related_name': 'reports', 'verbose_name': 'Report', 'verbose_name_plural': 'Reports'},
        ),
        migrations.AlterField(
            model_name='report',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='reports', to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='report',
            name='created_groups',
            field=models.ManyToManyField(blank=True, help_text='select all groups that apply, if any', limit_choices_to={'can_report_missing': True}, related_name='reports', to='mapdata.LocationGroup', verbose_name='location groups'),
        ),
    ]
