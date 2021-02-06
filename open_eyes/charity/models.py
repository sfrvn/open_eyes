from datetime import date

from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    title = models.CharField('Название', max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class HelpType(models.Model):
    title = models.CharField('Тип помощи', max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип помощи'
        verbose_name_plural = 'Типы помощи'


class Fund(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='funds',
    )
    name = models.CharField('Название', max_length=128)
    description = models.TextField('Описание')
    phone = models.CharField('Телефон', max_length=32)
    url = models.CharField('Ссылка', max_length=128)
    city = models.CharField(
        'Город', max_length=128, blank=True, null=True, default=''
    )
    categories = models.ManyToManyField(
        Category, verbose_name='Категории', related_name='funds'
    )
    logo = models.ImageField(
        'Логотип', upload_to='logo/', blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фонд'
        verbose_name_plural = 'Фонды'


class Project(models.Model):
    name = models.CharField('Название', max_length=128)
    description = models.TextField('Описание')
    short_description = models.TextField('Краткое писание', max_length=128)
    fund = models.ForeignKey(
        Fund, on_delete=models.CASCADE, related_name='projects'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='projects',
    )
    help_type = models.ForeignKey(
        HelpType, on_delete=models.SET_NULL, blank=True, null=True
    )
    help_description = models.CharField(
        'Описание помощи', max_length=64, blank=True, null=True
    )
    main_image = models.ImageField(
        'Изображение', upload_to='project_img/', blank=True, null=True
    )
    city = models.CharField(
        'Город', max_length=128, blank=True, null=True, default=''
    )
    published_at = models.DateField('Дата публикации', default=date.today)
    is_archived = models.BooleanField('В архиве', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проект'


class ProjectImage(models.Model):
    image = models.ImageField('Изображение', upload_to='project_img/')
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='additional_images'
    )

    class Meta:
        verbose_name = 'Доп. изображение'
        verbose_name_plural = 'Доп. изображения'
