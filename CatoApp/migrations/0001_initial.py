# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 22:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('company', models.CharField(max_length=256)),
                ('last_updated', models.DateField(auto_now=True)),
                ('posting_date', models.DateField(null=True)),
                ('valid', models.BooleanField(default=True)),
                ('zipcode', models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobNeedSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CatoApp.Job')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=256)),
                ('password', models.CharField(max_length=16)),
                ('education', models.CharField(choices=[('HI', 'High school'), ('UG', 'Undergraduate student'), ('BC', 'Bachelor'), ('GD', 'Graduate student'), ('MA', 'Master'), ('PD', 'PHD student'), ('DC', 'Doctor')], default='UG', max_length=2)),
                ('graduation_date', models.DateField(null=True)),
                ('major', models.CharField(max_length=16, null=True)),
                ('zipcode', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserHasSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CatoApp.Skill')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CatoApp.User')),
            ],
        ),
        migrations.CreateModel(
            name='UserJobRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seen', models.BooleanField(default=False)),
                ('recommended', models.BooleanField(default=False)),
                ('starred', models.BooleanField(default=False)),
                ('dismissed', models.BooleanField(default=False)),
                ('viewed_count', models.PositiveIntegerField(default=0)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CatoApp.Job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CatoApp.User')),
            ],
        ),
        migrations.AddField(
            model_name='jobneedskill',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CatoApp.Skill'),
        ),
    ]
