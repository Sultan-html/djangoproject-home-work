from django.db import models

# Create your models here.
class Employee(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок сайта'
    )
    description = models.TextField(
        verbose_name='Описание сайта'
    )
    russia = models.ImageField(
        upload_to='logo_image/'
    )
    s_russia = models.ImageField(
        upload_to='logo_image/'
    )
    bell = models.ImageField(
        upload_to='logo_image/'
    )
    s_bell = models.ImageField(
        upload_to='logo_image/'
    )
    Us = models.ImageField(
        upload_to='logo_image/'
    )
    s_us = models.ImageField(
        upload_to='logo_image/'
    )
    bio = models.TextField(
        verbose_name='Bio'
    )
    bio2 = models.TextField(
        verbose_name='Bio'
    )
    bio3 = models.TextField(
        verbose_name='Bio'
    )
    bio4 = models.TextField(
        verbose_name='Bio'
    )
    bio5 = models.TextField(
        verbose_name='Bio'
    )
    bio6 = models.TextField(
        verbose_name='Bio'
    )
