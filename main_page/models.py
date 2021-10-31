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


class Services(models.Model):
    title = models.TextField(verbose_name='Заголовок услуги', blank=False)
    link = models.TextField(verbose_name='Ссылка на страницу услуги', blank=False)

    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.title


# class Counter(models.Model):
#     title = models.CharField(max_length=200, verbose_name='Заголовок результата', blank=False)
#     value = models.DecimalField(verbose_name='Результативное число', max_digits=10000, decimal_places=0, blank=False)
#     logo = models.ImageField(upload_to='media', verbose_name='Иконка', blank=False)

#     class Meta:
#         verbose_name = 'Результат работы'
#         verbose_name_plural = 'Результаты работы'

#     def __str__(self):
#         return self.title


class WorkSteps(models.Model):
    number = models.DecimalField(verbose_name='Этап работы (число)', max_digits=10, decimal_places=0, blank=False)
    title = models.CharField(verbose_name='Заголовок этапа работы', max_length=500, blank=False)
    subtitle = models.CharField(verbose_name='Подзаголовок этапа работы', max_length=500, blank=True)
    text = models.TextField(verbose_name='Этап работы (текст)', blank=False)

    class Meta:
        verbose_name = 'Этап работы'
        verbose_name_plural = 'Этапы работы'

    def __str__(self):
        return f'{self.number} этап'


class CaseTitle(models.Model):
    title = models.CharField(max_length=200, verbose_name='Кейс для фирмы', blank=False)

    class Meta:
        verbose_name = 'Кейс'
        verbose_name_plural = 'Кейсы'

    def __str__(self):
        return self.title


class CaseImages(models.Model):
    case = models.ForeignKey(CaseTitle, on_delete=models.CASCADE, verbose_name='Для кейса', default=None)
    img = models.ImageField(upload_to='media', verbose_name='Баннер кейса', blank=False)

    def __str__(self):
        return self.case.title

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'

        

class MetaTags(models.Model):
    title = models.CharField(max_length=300, verbose_name='Title', blank=False)
    keywords = models.TextField(verbose_name='Keywords (Через запятую/Предложением)', blank=False)
    description = models.TextField(verbose_name='Description', blank=False)
    
    class Meta:
        verbose_name = 'Мета тег'
        verbose_name_plural = 'Мета теги'
        
    def __str__(self):
        return self.title
