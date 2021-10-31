from django.db import models


class MainBanner(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок', blank=False)
    subtitle = models.CharField(max_length=200, verbose_name='Подзаголовок', blank=True)
    logo = models.ImageField(upload_to='media', verbose_name='Баннер', blank=True)

    class Meta:
        verbose_name = 'Главный баннер'
        verbose_name_plural = 'Главные баннеры'

    def __str__(self):
        return self.title


class MiniBanner(models.Model):
    desktop = models.ImageField(upload_to='media', verbose_name='Мини-баннер', blank=True)
    mobile = models.ImageField(upload_to='media', verbose_name='Мини-баннер для мобильных устройств', blank=True)

    class Meta:
        verbose_name = 'Мини-баннер'
        verbose_name_plural = 'Мини-баннеры'

    def __str__(self):
        return 'Мини-баннер'
        
        
class WorkSteps(models.Model):
    title = models.CharField(verbose_name='Заголовок этапа работы', max_length=500, blank=False)
    text = models.TextField(verbose_name='Этап работы (текст)', blank=True)

    class Meta:
        verbose_name = 'Этап работы'
        verbose_name_plural = 'Этапы работы'

    def __str__(self):
        return self.title
        

class MetaTags(models.Model):
    title = models.CharField(max_length=300, verbose_name='Title', blank=False)
    keywords = models.TextField(verbose_name='Keywords (Через запятую/Предложением)', blank=False)
    description = models.TextField(verbose_name='Description', blank=False)
    
    class Meta:
        verbose_name = 'Мета тег'
        verbose_name_plural = 'Мета теги'
        
    def __str__(self):
        return self.title
