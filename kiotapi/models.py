from django.db import models


class ThoiGian(models.Model):
    CheDoTimKiem = models.BooleanField(default=False)
    ThoiGianBatDau = models.DateField(max_length=255)
    THoiGianKetThuc = models.DateField(max_length=255)
