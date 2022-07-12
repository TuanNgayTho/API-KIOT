from django.db import models


class ThoiGian(models.Model):
    ToDay = models.BooleanField(default=False)
    ThisWeek = models.BooleanField(default=False)
    ThisMonth = models.BooleanField(default=False)
    CheDoTimKiem = models.BooleanField(default=False)
    ThoiGianBatDau = models.DateField(max_length=255)
    THoiGianKetThuc = models.DateField(max_length=255)
