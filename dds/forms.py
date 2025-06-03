from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Status, Type, Category, SubCategory, CashFlowRecord

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']
        labels = {'name': _('Название статуса')}

class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']
        labels = {'name': _('Название типа')}

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'type']
        labels = {'name': _('Название категории'), 'type': _('Тип')}

class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['name', 'category']
        labels = {'name': _('Название подкатегории'), 'category': _('Категория')}

class CashFlowRecordForm(forms.ModelForm):
    class Meta:
        model = CashFlowRecord
        fields = ['date', 'status', 'type', 'category', 'subcategory', 'amount', 'comment']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'comment': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'date': _('Дата'),
            'status': _('Статус'),
            'type': _('Тип'),
            'category': _('Категория'),
            'subcategory': _('Подкатегория'),
            'amount': _('Сумма'),
            'comment': _('Комментарий'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()  # Allow all categories initially
        self.fields['subcategory'].queryset = SubCategory.objects.none()

        if 'type' in self.data:
            try:
                type_id = int(self.data.get('type'))
                self.fields['category'].queryset = Category.objects.filter(type_id=type_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['category'].queryset = Category.objects.filter(type=self.instance.type)

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = SubCategory.objects.filter(category_id=category_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['subcategory'].queryset = SubCategory.objects.filter(category=self.instance.category)