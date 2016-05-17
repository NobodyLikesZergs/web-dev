# coding: utf-8

from __future__ import unicode_literals
from django.db import models
from django.conf import settings

# Create your models here.


class Question(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               verbose_name=u'Автор поста')
    title = models.CharField(max_length=255, verbose_name=u'Заголовок вопроса')
    text = models.TextField(verbose_name=u'Текст вопроса')
    created_at = models.DateField(auto_now_add=True,
                                  verbose_name=u'Дата создания')
    modified_at = models.DateField(auto_now=True,
                                   verbose_name=u'Дата редактирования')

    class Meta:
        verbose_name = u'Вопрос'
        verbose_name_plural = u'Вопросы'
