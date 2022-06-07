# pip install djangorestframework
from rest_framework.serializers import ModelSerializer
from .models import customers


class CourseSerializer(ModelSerializer):
    class Meta:
        model = customers
        fields = ['id', 'customer', 'time', 'seller']
