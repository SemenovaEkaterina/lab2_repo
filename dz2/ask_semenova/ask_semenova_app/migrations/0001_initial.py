# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-14 17:34
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
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст ответа')),
                ('is_correct', models.BooleanField(verbose_name='Верно')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.BooleanField(verbose_name='+1')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст вопроса')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ask_semenova_app.Profile', verbose_name='Автор вопроса')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Тэг')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(to='ask_semenova_app.Tag'),
        ),
        migrations.AddField(
            model_name='like',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ask_semenova_app.Profile', verbose_name='Поставил лайк'),
        ),
        migrations.AddField(
            model_name='like',
            name='to_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ask_semenova_app.Question', verbose_name='Получил лайк'),
        ),
        migrations.AddField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ask_semenova_app.Profile', verbose_name='Автор ответа'),
        ),
    ]
