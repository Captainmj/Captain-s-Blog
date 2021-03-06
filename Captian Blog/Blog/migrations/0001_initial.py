# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-20 14:11
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
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='标题')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published'), ('personal', 'Personal')], default='draft', max_length=10, verbose_name='文章状态')),
                ('slug', models.SlugField(max_length=250, unique_for_date='created', verbose_name='标签')),
                ('body', models.TextField(verbose_name='正文')),
                ('topped', models.BooleanField(default=False, verbose_name='置顶')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='浏览量')),
                ('likes', models.PositiveIntegerField(default=0, verbose_name='点赞数')),
                ('abstract', models.CharField(blank=True, help_text='可选，如若为空将摘取正文的前54个字符', max_length=54, null=True, verbose_name='摘要')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name_plural': '文章',
                'ordering': ('-created',),
            },
        ),
    ]
