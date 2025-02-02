# Generated by Django 5.0.6 on 2024-06-11 16:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_user_is_active_user_is_staff_alter_user_is_superuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConferenceAgenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConferenceSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='logo/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('job', models.CharField(max_length=150)),
                ('desc', models.TextField()),
                ('img', models.ImageField(upload_to='member/')),
                ('type', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='PartAgenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('agend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.conferenceagenda')),
            ],
        ),
    ]
