# Generated by Django 3.2.4 on 2021-08-06 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('target', '0008_alter_tariffs_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tariffs',
            name='price',
            field=models.CharField(default='0', max_length=11, verbose_name='Цена'),
        ),
    ]
