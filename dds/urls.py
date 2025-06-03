from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('record/add/', views.record_form, name='record_add'),
    path('record/edit/<int:record_id>/', views.record_form, name='record_edit'),
    path('record/delete/<int:record_id>/', views.record_delete, name='record_delete'),
    path('get_categories/', views.get_categories, name='get_categories'),
    path('subcategories/', views.get_subcategories, name='get_subcategories'),
    path('dictionary/', views.dictionary_management, name='dictionary_management'),
    path('status/delete/<int:status_id>/', views.status_delete, name='status_delete'),
    path('type/delete/<int:type_id>/', views.type_delete, name='type_delete'),
    path('category/delete/<int:category_id>/', views.category_delete, name='category_delete'),
    path('subcategory/delete/<int:subcategory_id>/', views.subcategory_delete, name='subcategory_delete'),
]