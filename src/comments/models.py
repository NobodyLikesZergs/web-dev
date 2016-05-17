# coding: utf-8

from __future__ import unicode_literals
from django.db import models
from django.conf import settings

# Create your models here.


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               verbose_name=u'Автор комментария')
    text = models.CharField(max_length=255, verbose_name=u'Текст комментария')
    created_at = models.DateField(auto_now_add=True,
                                  verbose_name=u'Дата создания')
    modified_at = models.DateField(auto_now=True,
                                   verbose_name=u'Дата редактирования')
    parent_question = models.ForeignKey('questions.Question',
                                        verbose_name=u'Родительский вопрос')

    class Meta:
        verbose_name = u'Комментарий'
        verbose_name_plural = u'Комментарии'
