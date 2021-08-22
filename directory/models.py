from django.db import models
from django.contrib.auth.models import User

class Firm(models.Model):
    name = models.CharField(max_length=255, verbose_name='Организация')
    inn = models.CharField(max_length=12, verbose_name='ИНН')
    ogrn = models.CharField(max_length=13, verbose_name='ОГРН')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    phone = models.CharField(max_length=24, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email')

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организация'

    def __str__(self):
        return f'Организация {self.name} ИНН:{self.inn}'


class Office(models.Model):
    name = models.CharField(max_length=255, verbose_name='Офис/Мастерская')
    address = models.CharField(max_length=255, verbose_name='Адрес/Место')

    class Meta:
        verbose_name = 'Офис'
        verbose_name_plural = 'Офисы'

    def __str__(self):
        return f'{self.name}'


class Position(models.Model):
    name = models.CharField(max_length=255, verbose_name='Должность')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return f'{self.name}'

class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255, verbose_name='Сотрудник')
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    phone = models.CharField(max_length=24, verbose_name='Телефон')
    email = models.EmailField(verbose_name='E-mail')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.position} {self.name}'

class Customer(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    phone = models.CharField(max_length=14, verbose_name='Телефон')
    address = models.CharField(max_length=255, verbose_name='Адрес')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.name} {self.phone}'

