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


class WorkStrategy(models.Model):
    number = models.DecimalField(verbose_name='Номер по порядку', max_digits=10, decimal_places=0, blank=False)
    for_business = models.CharField(max_length=400, verbose_name='Для какого бизнеса?')
    title = models.CharField(verbose_name='Заголовок стратегии', max_length=500, blank=False)
    subtitle = models.CharField(verbose_name='Подзаголовок стратегии', max_length=500, blank=False)
    text = models.TextField(verbose_name='Описание', blank=False)

    class Meta:
        verbose_name = 'Стратегию работы'
        verbose_name_plural = 'Стратегия работы'

    def __str__(self):
        return f'{self.number}. {self.title}'


class Tariffs(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название', blank=False)
    bonus = models.CharField(max_length=400, verbose_name='Бонусы при приобретении этого тарифа', blank=True)
    price = models.CharField(max_length=11, verbose_name='Цена', blank=False, default='0')

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'

    def __str__(self):
        return self.title


class TariffList(models.Model):
    tariff = models.ForeignKey(Tariffs, on_delete=models.CASCADE, verbose_name='Для тарифа', default=None)
    list = models.CharField(max_length=250, verbose_name='Что в себя включает?', blank=False)

    class Meta:
        verbose_name = 'Список услуг'
        verbose_name_plural = 'Список услуг'

    def __str__(self):
        return self.tariff.title

        

class MetaTags(models.Model):
    title = models.CharField(max_length=300, verbose_name='Title', blank=False)
    keywords = models.TextField(verbose_name='Keywords (Через запятую/Предложением)', blank=False)
    description = models.TextField(verbose_name='Description', blank=False)
    
    class Meta:
        verbose_name = 'Мета тег'
        verbose_name_plural = 'Мета теги'
        
    def __str__(self):
        return self.title

