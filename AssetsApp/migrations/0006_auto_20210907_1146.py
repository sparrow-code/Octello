# Generated by Django 3.2.5 on 2021-09-07 11:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AssetsApp', '0005_auto_20210906_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetscategories',
            name='datetime_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 7, 11, 46, 5, 971469)),
        ),
        migrations.AlterField(
            model_name='assetscategories',
            name='parent_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AssetsApp.assetscategories'),
        ),
    ]