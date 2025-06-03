from rest_framework import serializers
from .models import Status, Type, Category, SubCategory, CashFlowRecord

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'name']

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    type_id = serializers.PrimaryKeyRelatedField(queryset=Type.objects.all(), source='type')

    class Meta:
        model = Category
        fields = ['id', 'name', 'type_id']

class SubCategorySerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category')

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category_id']

class CashFlowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashFlowRecord
        fields = ['id', 'date', 'status', 'type', 'category', 'subcategory', 'amount', 'comment']