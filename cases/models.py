from django.db import models
from .ru_to_eng import translate
from django.urls import reverse


class MainBanner(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок', blank=False)
    subtitle = models.CharField(max_length=200, verbose_name='Подзаголовок', blank=True)
    logo = models.ImageField(upload_to='media', verbose_name='Баннер', blank=True)

    class Meta:
        verbose_name = 'Главный баннер'
        verbose_name_plural = 'Главные баннеры'

    def __str__(self):
        return self.title
      
      
class CaseCategory(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', blank=False, unique=True)
    slug = models.CharField(max_length=200, verbose_name='slug (Не обязательно)', blank=True, unique=True)
    
    class Meta:
        verbose_name = 'Название категории'
        verbose_name_plural = 'Название категорий'
    
    def __str__(self):
        return self.title
    
    def get_url(self):
        return reverse("cases_slug", args=[self.slug])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = translate(self.title)
        super().save(*args, **kwargs)
        
        
class Case(models.Model):
    category = models.ForeignKey(CaseCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, verbose_name='Название кейса', blank=False)
    img = models.ImageField(upload_to='media', verbose_name='Картинка', blank=False)
    
    class Meta:
        verbose_name = 'Кейс'
        verbose_name_plural = 'Кейсы'
        
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
      