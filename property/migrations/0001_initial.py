# Generated by Django 5.0.7 on 2024-08-03 11:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=200, verbose_name='ФИО владельца')),
                ('owners_phonenumber', models.CharField(max_length=20, verbose_name='Номер владельца')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='Когда создано объявление')),
                ('description', models.TextField(blank=True, verbose_name='Текст объявления')),
                ('price', models.IntegerField(db_index=True, verbose_name='Цена квартиры')),
                ('town', models.CharField(db_index=True, max_length=50, verbose_name='Город, где находится квартира')),
                ('town_district', models.CharField(blank=True, help_text='Чертаново Южное', max_length=50, verbose_name='Район города, где находится квартира')),
                ('address', models.TextField(help_text='ул. Подольских курсантов д.5 кв.4', verbose_name='Адрес квартиры')),
                ('floor', models.CharField(help_text='Первый этаж, последний этаж, пятый этаж', max_length=3, verbose_name='Этаж')),
                ('rooms_number', models.IntegerField(db_index=True, verbose_name='Количество комнат в квартире')),
                ('living_area', models.IntegerField(blank=True, db_index=True, null=True, verbose_name='количество жилых кв.метров')),
                ('has_balcony', models.BooleanField(db_index=True, verbose_name='Наличие балкона')),
                ('active', models.BooleanField(db_index=True, verbose_name='Активно-ли объявление')),
                ('construction_year', models.IntegerField(blank=True, db_index=True, null=True, verbose_name='Год постройки здания')),
            ],
        ),
    ]
