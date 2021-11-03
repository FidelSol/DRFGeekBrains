from django.db import models
from apipoint.models import CustomUser


class Project(models.Model):
    url = models.URLField('Ссылка', max_length=254, unique=True, null=True)
    name = models.CharField('Название', max_length=30)
    users = models.ManyToManyField(CustomUser, blank=True, related_name='users', verbose_name="Набор пользователей")

    objects = models.Manager()

    def __str__(self):
        return self.name

class ToDo(models.Model):
    text = models.TextField('Содержание')
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True,  blank=True, related_name='todos', verbose_name="Набор пользователей")
    add_time = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="Дата создания")
    mod_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Дата изменения")
    creator = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='todos', verbose_name="Создатель")
    status = models.BooleanField(default=True, verbose_name="Создатель")

    objects = models.Manager()

    def __str__(self):
        return f'{self.add_time} - {self.creator.username}'
