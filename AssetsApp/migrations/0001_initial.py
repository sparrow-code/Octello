# Generated by Django 3.1.5 on 2021-08-30 14:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssetsCategories',
            fields=[
                ('id', models.PositiveIntegerField(editable=False, primary_key=True, serialize=False)),
                ('parent_id', models.PositiveIntegerField(null=True)),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_sub_category', models.BooleanField()),
                ('datetime_added', models.DateTimeField(default=datetime.datetime(2021, 8, 30, 16, 46, 49, 869125))),
            ],
        ),
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('asset_id', models.CharField(editable=False, max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=50)),
                ('class_term', models.CharField(max_length=15)),
                ('status', models.CharField(help_text='0 Is Inservice, 1 is Inactive and 3 Under Maintaince', max_length=20)),
                ('currency', models.CharField(max_length=5, null=True)),
                ('datetime_added', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AssetsApp.assetscategories')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_category', to='AssetsApp.assetscategories')),
            ],
        ),
    ]
