# Generated by Django 4.2.7 on 2024-02-15 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series_reference', models.CharField(max_length=100)),
                ('series_num', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_value', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(max_length=100)),
                ('units', models.CharField(max_length=100)),
                ('magnitude', models.IntegerField()),
                ('subject', models.CharField(max_length=200)),
                ('group', models.CharField(max_length=100)),
                ('series_title1', models.CharField(max_length=100)),
                ('series_title2', models.CharField(max_length=100)),
                ('series_title3', models.CharField(max_length=100)),
            ],
        ),
    ]