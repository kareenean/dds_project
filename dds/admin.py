from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Status, Type, Category, SubCategory, CashFlowRecord

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['name']
    verbose_name = _('Статус')
    verbose_name_plural = _('Статусы')

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    verbose_name = _('Тип')
    verbose_name_plural = _('Типы')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']
    list_filter = ['type']
    verbose_name = _('Категория')
    verbose_name_plural = _('Категории')

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_filter = ['category']
    verbose_name = _('Подкатегория')
    verbose_name_plural = _('Подкатегории')

@admin.register(CashFlowRecord)
class CashFlowRecordAdmin(admin.ModelAdmin):
    list_display = ['date', 'status', 'type', 'category', 'subcategory', 'amount']
    list_filter = ['date', 'status', 'type', 'category', 'subcategory']
    verbose_name = _('Запись ДДС')
    verbose_name_plural = _('Записи ДДС')