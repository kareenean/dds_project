from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Status(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name=_('Статус'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Статус')
        verbose_name_plural = _('Статусы')

class Type(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name=_('Тип'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Тип')
        verbose_name_plural = _('Типы')

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_('Категория'))
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='categories', verbose_name=_('Тип'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

class SubCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_('Подкатегория'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories', verbose_name=_('Категория'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Подкатегория')
        verbose_name_plural = _('Подкатегории')

class CashFlowRecord(models.Model):
    date = models.DateField(default=timezone.now, verbose_name=_('Дата'))
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name=_('Статус'))
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name=_('Тип'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Категория'))
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name=_('Подкатегория'))
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], verbose_name=_('Сумма'))
    comment = models.TextField(blank=True, null=True, verbose_name=_('Комментарий'))

    def __str__(self):
        return f"{self.date} - {self.amount} - {self.category}"

    class Meta:
        verbose_name = _('Запись ДДС')
        verbose_name_plural = _('Записи ДДС')