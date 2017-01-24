from django.db import models

# Create your models here.


class Topics(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

class Topic(models.Model):
    title = models.ForeignKey(Topics, verbose_name='Тема')
    sub_title = models.CharField(max_length=100, verbose_name='Заголовок')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    text = models.TextField(verbose_name='Текст статьи')


