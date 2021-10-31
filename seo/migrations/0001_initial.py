# Generated by Django 3.2.4 on 2021-07-24 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('subtitle', models.CharField(blank=True, max_length=200, verbose_name='Подзаголовок')),
                ('logo', models.ImageField(blank=True, upload_to='media', verbose_name='Баннер')),
            ],
            options={
                'verbose_name': 'Главный баннер',
                'verbose_name_plural': 'Главные баннеры',
            },
        ),
        migrations.CreateModel(
            name='MiniBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, upload_to='media', verbose_name='Мини-баннер')),
                ('mobile_img', models.ImageField(blank=True, upload_to='media', verbose_name='Мини-баннер для мобильных устройств')),
            ],
            options={
                'verbose_name': 'Мини-баннер',
                'verbose_name_plural': 'Мини-баннеры',
            },
        ),
    ]
