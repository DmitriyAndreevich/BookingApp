# Generated by Django 2.2.4 on 2019-09-19 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0010_auto_20190919_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_list',
            name='post_detail_description',
            field=models.TextField(blank=True, default=None, max_length=1024, null=True),
        ),
    ]
