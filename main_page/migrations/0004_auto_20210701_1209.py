# Generated by Django 3.2.4 on 2021-07-01 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_auto_20210701_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainbanner',
            name='main_banner_logo',
            field=models.ImageField(blank=True, upload_to='media', verbose_name='Иконка на баннере'),
        ),
        migrations.AlterField(
            model_name='mainbanner',
            name='main_banner_gif',
            field=models.FileField(blank=True, upload_to='media', verbose_name='Гиф на главном баннере'),
        ),
        migrations.AlterField(
            model_name='mainbanner',
            name='main_banner_subtitle',
            field=models.CharField(blank=True, max_length=200, verbose_name='Подзаголовок главного баннера'),
        ),
    ]
