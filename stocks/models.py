from django.db import models


class Branches(models.Model):
    branch = models.CharField(max_length=50, verbose_name='Филиал')
    adress = models.CharField(max_length=250, verbose_name='Адрес')


class Coast(models.Model):
    branch = models.ForeignKey('Branches', on_delete=models.CASCADE, verbose_name='Филиал')
    type_of_abonem = models.CharField(max_length=50, verbose_name='Тип Абонемента')
    coast = models.IntegerField(verbose_name='Цена Абонемента')


class Timetable(models.Model):
    branch = models.ForeignKey('Branches', on_delete=models.CASCADE, verbose_name='Филиал')
    group_name = models.CharField(max_length=50, verbose_name='Название группы')
    day = models.CharField(max_length=50, verbose_name='День недели когда занимается группа')
    time = models.TimeField(verbose_name='Время занятия')
    age = models.IntegerField(verbose_name='Возраст детей на занятии')
