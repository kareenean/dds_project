from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import CashFlowRecord, Status, Type, Category, SubCategory
from .forms import CashFlowRecordForm, StatusForm, TypeForm, CategoryForm, SubCategoryForm
from django.http import JsonResponse
from django.db.models import Q
from datetime import datetime

def index(request):
    records = CashFlowRecord.objects.all()
    
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    if start_date:
        records = records.filter(date__gte=start_date)
    if end_date:
        records = records.filter(date__lte=end_date)
    
    status_id = request.GET.get('status')
    if status_id:
        records = records.filter(status_id=status_id)
    
    type_id = request.GET.get('type')
    if type_id:
        records = records.filter(type_id=type_id)
    
    category_id = request.GET.get('category')
    if category_id:
        records = records.filter(category_id=category_id)
    
    subcategory_id = request.GET.get('subcategory')
    if subcategory_id:
        records = records.filter(subcategory_id=subcategory_id)
    
    statuses = Status.objects.all()
    types = Type.objects.all()
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    
    context = {
        'records': records,
        'statuses': statuses,
        'types': types,
        'categories': categories,
        'subcategories': subcategories,
        'start_date': start_date or '',
        'end_date': end_date or '',
        'selected_status': int(status_id) if status_id else None,
        'selected_type': int(type_id) if type_id else None,
        'selected_category': int(category_id) if category_id else None,
        'selected_subcategory': int(subcategory_id) if subcategory_id else None,
    }
    return render(request, 'index.html', context)

def record_form(request, record_id=None):
    if record_id:
        record = get_object_or_404(CashFlowRecord, id=record_id)
        form = CashFlowRecordForm(request.POST or None, instance=record)
    else:
        form = CashFlowRecordForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Запись успешно сохранена.")
        return redirect('index')

    return render(request, 'record_form.html', {'form': form})

def record_delete(request, record_id):
    if request.method == 'POST':
        record = get_object_or_404(CashFlowRecord, id=record_id)
        record.delete()
        messages.success(request, "Запись успешно удалена.")
        return redirect('index')
    return redirect('index')

def dictionary_management(request):
    if request.method == 'POST':
        if 'status_submit' in request.POST:
            status_form = StatusForm(request.POST)
            if status_form.is_valid():
                status_form.save()
                messages.success(request, "Статус добавлен.")
                return redirect('dictionary_management')
        elif 'type_submit' in request.POST:
            type_form = TypeForm(request.POST)
            if type_form.is_valid():
                type_form.save()
                messages.success(request, "Тип добавлен.")
                return redirect('dictionary_management')
        elif 'category_submit' in request.POST:
            category_form = CategoryForm(request.POST)
            if category_form.is_valid():
                category_form.save()
                messages.success(request, "Категория добавлена.")
                return redirect('dictionary_management')
        elif 'subcategory_submit' in request.POST:
            subcategory_form = SubCategoryForm(request.POST)
            if subcategory_form.is_valid():
                subcategory_form.save()
                messages.success(request, "Подкатегория добавлена.")
                return redirect('dictionary_management')
    else:
        status_form = StatusForm()
        type_form = TypeForm()
        category_form = CategoryForm()
        subcategory_form = SubCategoryForm()

    statuses = Status.objects.all()
    types = Type.objects.all()
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()

    context = {
        'status_form': status_form,
        'type_form': type_form,
        'category_form': category_form,
        'subcategory_form': subcategory_form,
        'statuses': statuses,
        'types': types,
        'categories': categories,
        'subcategories': subcategories,
    }
    return render(request, 'dictionary_management.html', context)

def get_categories(request):
    type_id = request.GET.get('type_id')
    categories = Category.objects.filter(type_id=type_id).values('id', 'name')
    return JsonResponse({'categories': list(categories)})

def get_subcategories(request):
    category_id = request.GET.get('category_id')
    subcategories = SubCategory.objects.filter(category_id=category_id).values('id', 'name')
    return JsonResponse({'subcategories': list(subcategories)})

def status_delete(request, status_id):
    if request.method == 'POST':
        status = get_object_or_404(Status, id=status_id)
        status.delete()
        messages.success(request, "Статус успешно удален.")
        return redirect('dictionary_management')
    return redirect('dictionary_management')

def type_delete(request, type_id):
    if request.method == 'POST':
        type = get_object_or_404(Type, id=type_id)
        type.delete()
        messages.success(request, "Тип успешно удален.")
        return redirect('dictionary_management')
    return redirect('dictionary_management')

def category_delete(request, category_id):
    if request.method == 'POST':
        category = get_object_or_404(Category, id=category_id)
        category.delete()
        messages.success(request, "Категория успешно удалена.")
        return redirect('dictionary_management')
    return redirect('dictionary_management')

def subcategory_delete(request, subcategory_id):
    if request.method == 'POST':
        subcategory = get_object_or_404(SubCategory, id=subcategory_id)
        subcategory.delete()
        messages.success(request, "Подкатегория успешно удалена.")
        return redirect('dictionary_management')
    return redirect('dictionary_management')