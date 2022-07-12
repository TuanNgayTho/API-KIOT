# pip install djangorestframework

from rest_framework import serializers


class SnippetSerial(serializers.Serializer):
    customerName = serializers.CharField(required=False, allow_blank=True, max_length=100)
    purchaseDate = serializers.CharField(required=False, allow_blank=True, max_length=100)
    soldByName = serializers.CharField(required=False, allow_blank=True, max_length=100)
    statusValue = serializers.CharField(required=False, allow_blank=True, max_length=100)


class SnippetSerialthoigian(serializers.Serializer):
    ToDay = serializers.CharField(required=False, allow_blank=True, max_length=100)
    ThisWeek = serializers.CharField(required=False, allow_blank=True, max_length=100)
    ThisMonth = serializers.CharField(required=False, allow_blank=True, max_length=100)
    CheDoTimKiem = serializers.CharField(required=False, allow_blank=True, max_length=100)
    ThoiGianBatDau = serializers.CharField(required=False, allow_blank=True, max_length=100)
    THoiGianKetThuc = serializers.CharField(required=False, allow_blank=True, max_length=100)
