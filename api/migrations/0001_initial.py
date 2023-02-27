# Generated by Django 4.1.7 on 2023-02-27 15:15

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), size=None), size=None)),
                ('gbfs_href', models.URLField()),
                ('href', models.CharField(max_length=50)),
                ('location', models.JSONField()),
            ],
            options={
                'ordering': ['-name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(max_length=200)),
                ('region', models.CharField(max_length=200)),
                ('typology', models.CharField(max_length=200)),
                ('holder', models.CharField(max_length=200)),
                ('investment', models.CharField(max_length=200)),
                ('date_admission', models.DateField()),
                ('status', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['-name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('empty_slots', models.IntegerField()),
                ('extra', models.JSONField()),
                ('free_bikes', models.IntegerField()),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=10)),
                ('timestamp', models.DateTimeField()),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.network')),
            ],
            options={
                'ordering': ['-name'],
                'abstract': False,
            },
        ),
    ]
