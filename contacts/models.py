from django.db import models


class Phone(models.Model):
    phone_number = models.CharField(max_length=200, verbose_name='Телефон', blank=False)

    class Meta:
        verbose_name = 'Номер телефона'
        verbose_name_plural = 'Номера телефонов'

    def __str__(self):
        return self.phone_number


class Location(models.Model):
    location = models.TextField(verbose_name='Ссылка на локацию', blank=False)

    class Meta:
        verbose_name = 'Локацию'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return 'Геопозиция'


class Email(models.Model):
    email = models.CharField(max_length=200, verbose_name='Почта', blank=False)

    class Meta:
        verbose_name = 'Почту'
        verbose_name_plural = 'Почты'

    def __str__(self):
        return self.email


class Instagram(models.Model):
    link = models.TextField(verbose_name='Ссылка на Instagram аккаунт', blank=False)
    icon = models.ImageField(upload_to='media', verbose_name='Иконка', blank=False)

    class Meta:
        verbose_name = 'Instagram'
        verbose_name_plural = 'Instagram'

    def __str__(self):
        return self.link


class Telegram(models.Model):
    link = models.TextField(verbose_name='Ссылка на Telegram аккаунт', blank=False)
    icon = models.ImageField(upload_to='media', verbose_name='Иконка', blank=False)

    class Meta:
        verbose_name = 'Telegram'
        verbose_name_plural = 'Telegram'

    def __str__(self):
        return self.link


class Facebook(models.Model):
    link = models.TextField(verbose_name='Ссылка на Facebook аккаунт', blank=False)
    icon = models.ImageField(upload_to='media', verbose_name='Иконка', blank=False)

    class Meta:
        verbose_name = 'Facebook'
        verbose_name_plural = 'Facebook'

    def __str__(self):
        return self.link


class TikTok(models.Model):
    link = models.TextField(verbose_name='Ссылка на TikTok аккаунт', blank=False)
    icon = models.ImageField(upload_to='media', verbose_name='Иконка', blank=False)

    class Meta:
        verbose_name = 'TikTok'
        verbose_name_plural = 'TikTok'

    def __str__(self):
        return self.link


class YouTube(models.Model):
    link = models.TextField(verbose_name='Ссылка на YouTube аккаунт', blank=False)
    icon = models.ImageField(upload_to='media', verbose_name='Иконка', blank=False)

    class Meta:
        verbose_name = 'YouTube'
        verbose_name_plural = 'YouTube'

    def __str__(self):
        return self.link


class Address(models.Model):
    address = models.TextField(verbose_name='Адрес', blank=False)
    link = models.TextField(verbose_name='Ссылка на локацию', blank=True)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return self.address


class MetaTags(models.Model):
    title = models.CharField(max_length=300, verbose_name='Title', blank=False)
    keywords = models.TextField(verbose_name='Keywords (Через запятую/Предложением)', blank=False)
    description = models.TextField(verbose_name='Description', blank=False)
    
    class Meta:
        verbose_name = 'Мета тег'
        verbose_name_plural = 'Мета теги'
        
    def __str__(self):
        return self.title

