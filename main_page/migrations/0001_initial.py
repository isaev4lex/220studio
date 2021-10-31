# Generated by Django 3.2.4 on 2021-07-01 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter_logo', models.ImageField(upload_to='media', verbose_name='Иконка')),
                ('counter_value', models.DecimalField(decimal_places=5, max_digits=10000, verbose_name='Результативное число')),
                ('counter_title', models.TextField(verbose_name='Заголовок результата')),
            ],
        ),
        migrations.CreateModel(
            name='MainBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_banner_image', models.ImageField(upload_to='media', verbose_name='Картинка главного баннера')),
                ('main_banner_title', models.TextField(verbose_name='Заголовок главного баннера')),
                ('main_banner_subtitle', models.CharField(max_length=200, verbose_name='Подзаголовок главного баннера')),
                ('main_banner_gif', models.FileField(upload_to='media', verbose_name='Гиф на главном баннере')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_logo', models.TextField()),
                ('service_title', models.TextField(verbose_name='Заголовок услуги')),
                ('service_link', models.TextField(verbose_name='Ссылка на страницу услуги')),
            ],
        ),
        migrations.CreateModel(
            name='WorkSteps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workstep_number', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Этап работы (число)')),
                ('workstep_text', models.TextField(verbose_name='Этап работы (текст)')),
            ],
        ),
    ]
