# pip install djangorestframework

from rest_framework import serializers


class SnippetSerial(serializers.Serializer):
    customerName = serializers.CharField(required=False, allow_blank=True, max_length=100)
    purchaseDate = serializers.CharField(required=False, allow_blank=True, max_length=100)
    soldByName = serializers.CharField(required=False, allow_blank=True, max_length=100)
    statusValue = serializers.CharField(required=False, allow_blank=True, max_length=100)
