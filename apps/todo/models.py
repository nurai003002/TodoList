from django.db import models

# Create your models here.
class Task(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название'
    )
    description = models.TextField(
        verbose_name = 'Описание'
    )
    completed = models.BooleanField(
        default = False,
        verbose_name = 'Статус'
    )
    created = models.DateTimeField(
        auto_now_add = True,
        verbose_name = 'Время создания'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
