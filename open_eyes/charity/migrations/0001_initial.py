# Generated by Django 3.1.6 on 2021-02-06 00:15

import datetime
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
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('phone', models.CharField(max_length=32, verbose_name='Телефон')),
                ('url', models.CharField(max_length=128, verbose_name='Ссылка')),
                ('city', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='Город')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo/', verbose_name='Логотип')),
                ('categories', models.ManyToManyField(related_name='funds', to='charity.Category', verbose_name='Категории')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='funds', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Фонд',
                'verbose_name_plural': 'Фонды',
            },
        ),
        migrations.CreateModel(
            name='HelpType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Тип помощи')),
            ],
            options={
                'verbose_name': 'Тип помощи',
                'verbose_name_plural': 'Типы помощи',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('short_description', models.TextField(max_length=128, verbose_name='Краткое писание')),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='project_img/', verbose_name='Изображение')),
                ('city', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='Город')),
                ('published_at', models.DateField(default=datetime.date.today, verbose_name='Дата публикации')),
                ('is_archived', models.BooleanField(default=False, verbose_name='В архиве')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='charity.category')),
                ('fund', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='charity.fund')),
                ('help_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='charity.helptype')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проект',
            },
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='project_img/', verbose_name='Изображение')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='additional_images', to='charity.project')),
            ],
            options={
                'verbose_name': 'Доп. изображение',
                'verbose_name_plural': 'Доп. изображения',
            },
        ),
    ]
