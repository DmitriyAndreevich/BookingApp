# Generated by Django 2.2.4 on 2019-09-08 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0006_auto_20190907_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='day1_head',
            field=models.TextField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='tour',
            name='day2_head',
            field=models.TextField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='tour',
            name='day3_head',
            field=models.TextField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='tour',
            name='day4_head',
            field=models.TextField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='tour',
            name='day5_head',
            field=models.TextField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
