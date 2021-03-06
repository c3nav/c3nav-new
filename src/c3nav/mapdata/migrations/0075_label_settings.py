# Generated by Django 2.2.8 on 2019-12-21 23:27

import c3nav.mapdata.fields
from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mapdata', '0074_show_labels'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabelSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', c3nav.mapdata.fields.I18nField(fallback_any=True, plural_name='titles', verbose_name='Title')),
                ('min_zoom', models.DecimalField(decimal_places=1, default=-10, max_digits=3, validators=[django.core.validators.MinValueValidator(Decimal('-10')), django.core.validators.MaxValueValidator(Decimal('10'))], verbose_name='min zoom')),
                ('max_zoom', models.DecimalField(decimal_places=1, default=10, max_digits=3, validators=[django.core.validators.MinValueValidator(Decimal('-10')), django.core.validators.MaxValueValidator(Decimal('10'))], verbose_name='max zoom')),
                ('font_size', models.IntegerField(default=12, validators=[django.core.validators.MinValueValidator(12), django.core.validators.MaxValueValidator(30)], verbose_name='font size')),
            ],
            options={
                'verbose_name': 'Label Settings',
                'verbose_name_plural': 'Label Settings',
                'default_related_name': 'labelsettings',
            },
        ),
        migrations.RemoveField(
            model_name='area',
            name='show_label',
        ),
        migrations.RemoveField(
            model_name='level',
            name='show_label',
        ),
        migrations.RemoveField(
            model_name='locationgroup',
            name='show_labels',
        ),
        migrations.RemoveField(
            model_name='poi',
            name='show_label',
        ),
        migrations.RemoveField(
            model_name='space',
            name='show_label',
        ),
        migrations.AddField(
            model_name='area',
            name='label_override',
            field=c3nav.mapdata.fields.I18nField(blank=True, fallback_any=True, plural_name='label_overrides', verbose_name='Label override'),
        ),
        migrations.AddField(
            model_name='level',
            name='label_override',
            field=c3nav.mapdata.fields.I18nField(blank=True, fallback_any=True, plural_name='label_overrides', verbose_name='Label override'),
        ),
        migrations.AddField(
            model_name='poi',
            name='label_override',
            field=c3nav.mapdata.fields.I18nField(blank=True, fallback_any=True, plural_name='label_overrides', verbose_name='Label override'),
        ),
        migrations.AddField(
            model_name='space',
            name='label_override',
            field=c3nav.mapdata.fields.I18nField(blank=True, fallback_any=True, plural_name='label_overrides', verbose_name='Label override'),
        ),
        migrations.AddField(
            model_name='area',
            name='label_settings',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='areas', to='mapdata.LabelSettings', verbose_name='label settings'),
        ),
        migrations.AddField(
            model_name='level',
            name='label_settings',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='levels', to='mapdata.LabelSettings', verbose_name='label settings'),
        ),
        migrations.AddField(
            model_name='locationgroup',
            name='label_settings',
            field=models.ForeignKey(help_text='unless location specifies otherwise', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='locationgroups', to='mapdata.LabelSettings', verbose_name='label settings'),
        ),
        migrations.AddField(
            model_name='poi',
            name='label_settings',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pois', to='mapdata.LabelSettings', verbose_name='label settings'),
        ),
        migrations.AddField(
            model_name='space',
            name='label_settings',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='spaces', to='mapdata.LabelSettings', verbose_name='label settings'),
        ),
    ]
