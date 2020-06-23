# Generated by Django 3.0.7 on 2020-06-23 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200619_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='latitude',
            field=models.CharField(blank=True, default='', max_length=16),
        ),
        migrations.AddField(
            model_name='service',
            name='longitude',
            field=models.CharField(blank=True, default='', max_length=16),
        ),
        migrations.AlterField(
            model_name='service',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='service',
            name='operating_hours',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='service',
            name='phone_number',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='service',
            name='website',
            field=models.URLField(blank=True, default=''),
        ),
    ]
