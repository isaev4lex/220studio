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
    number = models.DecimalField(verbose_name='Этап работы (число)', max_digits=10, decimal_places=0, blank=False)
    text = models.TextField(verbose_name='Этап работы (текст)', blank=False)

    class Meta:
        verbose_name = 'Этап работы'
        verbose_name_plural = 'Этапы работы'

    def __str__(self):
        return f'{self.number} этап'


class ContextAdvertisementTools(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название инструмента')
    img = models.ImageField(upload_to='media', verbose_name='Логотип инструмента')

    class Meta:
        verbose_name = 'Инструмент контекстной рекламы'
        verbose_name_plural = 'Инструменты контекстной рекламы'

    def __str__(self):
        return self.title


class ContextAdvertisementDescription(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название инструмента')
    description = models.TextField(verbose_name='Описание инструмента\n\n(для переноса строки использовать <br>)')

    class Meta:
        verbose_name = 'Описание инструмента контекстной рекламы'
        verbose_name_plural = 'Описание инструментов контекстной рекламы'

    def __str__(self):
        return self.title


class ContextAdvertisementPossibilities(models.Model):
    tool = models.ForeignKey(ContextAdvertisementDescription, on_delete=models.CASCADE, verbose_name='Для инструмента', default=None)
    possibilities = models.CharField(max_length=300, verbose_name='Возможность инструмента')

    class Meta:
        verbose_name = 'Возможность инструмента контекстной рекламы'
        verbose_name_plural = 'Возможности инструментов контекстной рекламы'

    def __str__(self):
        return self.tool.title
        

class MetaTags(models.Model):
    title = models.CharField(max_length=300, verbose_name='Title', blank=False)
    keywords = models.TextField(verbose_name='Keywords (Через запятую/Предложением)', blank=False)
    description = models.TextField(verbose_name='Description', blank=False)
    
    class Meta:
        verbose_name = 'Мета тег'
        verbose_name_plural = 'Мета теги'
        
    def __str__(self):
        return self.title
