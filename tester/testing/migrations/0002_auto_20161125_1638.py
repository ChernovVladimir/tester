# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 14:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionSimple',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='testing.Question')),
            ],
            bases=('testing.question',),
        ),
        migrations.RenameModel(
            old_name='SimpleTestAnswer',
            new_name='Answer',
        ),
    ]