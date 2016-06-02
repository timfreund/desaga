# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 03:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('slug', models.CharField(max_length=128)),
                ('maximum_students', models.IntegerField()),
                ('start_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='LabParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LabType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('display_name', models.CharField(max_length=128)),
                ('implementation_class', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='LabTypeMetaparameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('display_name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=2048)),
                ('parameter_type', models.CharField(choices=[('INT', 'Integer'), ('STR', 'String'), ('BOOL', 'Boolean')], max_length=16)),
                ('lab_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='metaparameters', to='registrar.LabType')),
            ],
        ),
        migrations.CreateModel(
            name='SSHKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('fingerprint', models.CharField(max_length=48)),
                ('public_key', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StaffRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registrar.Lab')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('active', 'Active'), ('complete', 'Complete'), ('new', 'New'), ('waitlist', 'Wait list'), ('withdrawn', 'Withdrawn')], default='new', max_length=128)),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registrar.Lab')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='labparameter',
            name='meta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='registrar.LabTypeMetaparameter'),
        ),
        migrations.AddField(
            model_name='labparameter',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parameters', to='registrar.Lab'),
        ),
        migrations.AddField(
            model_name='lab',
            name='lab_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registrar.LabType'),
        ),
    ]