from django.db import models

import constants


# Create your models here.


class Product(models.Model):

    title = models.CharField(max_length=255, verbose_name='Продукт')
    model = models.CharField(max_length=255, verbose_name='Модель')
    date_created = models.DateField(verbose_name='Дата Выхода продукта на рынок')

    def __repr__(self):
        return f'{self.title} - {self.model}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Supplier(models.Model):

    title = models.CharField(max_length=150, verbose_name='Название')
    company_type = models.CharField(choices=constants.PROVIDER_CHOICES, verbose_name='Тип компании')
    email = models.EmailField(verbose_name='Адрес электронной почты')
    country = models.CharField(max_length=255, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=150, verbose_name='Улица')
    number_house = models.IntegerField(verbose_name='Номер дома')
    parent_supplier = models.ForeignKey('self', default=None,
                                        on_delete=models.CASCADE,
                                        verbose_name='Поставщик',
                                        **constants.NULLABLE,
                                        related_name='child_suppliers',)
    level = models.IntegerField(verbose_name='Уровень иерархии', default=0)
    time_created = models.TimeField(auto_now_add=True, verbose_name='Время создания')
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2,
                                           verbose_name='Задолежность перед поставщиком', **constants.NULLABLE)
    products = models.ForeignKey(Product, verbose_name='Продукты', on_delete=models.CASCADE,
                                 related_name='products')

    def __repr__(self):
        return f'{self.title}\n{self.email}\n{self.country}'

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def level_up(self):
        """ Устанавливаем/меняем уровень иерархии """
        if self.parent_supplier is None:
            if self.company_type == constants.FACTORY:
                self.level = 0
            elif self.company_type == constants.RETAIL:
                self.level = 1
            else:
                self.level = 2
        else:
            if self.company_type == constants.FACTORY:
                self.level = 0
            elif self.company_type == constants.RETAIL and self.parent_supplier.company_type == constants.ENTERPRENEUR:
                if self.parent_supplier.level == 2:
                    self.parent_supplier.level = 1
                self.level = 2
            elif self.company_type == constants.RETAIL and self.parent_supplier.company_type == constants.FACTORY:
                self.level = 1
            elif self.company_type == constants.ENTERPRENEUR and self.parent_supplier.company_type == constants.FACTORY:
                self.level = 1
            elif self.company_type == constants.ENTERPRENEUR and self.parent_supplier.company_type == constants.RETAIL:
                if self.parent_supplier.level != 1:
                    self.parent_supplier.level = 1
                self.level = 2
