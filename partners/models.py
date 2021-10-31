from django.db import models


class Cooperate(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название компании', blank=False)
    img = models.ImageField(upload_to='media', verbose_name='Лого компании', blank=False)

    class Meta:
        verbose_name = 'Партнёра'
        verbose_name_plural = 'Партнёры'

    def __str__(self):
        return self.title
