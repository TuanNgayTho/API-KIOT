from django.shortcuts import render
from django.views import View
import ReQuest
from rest_framework.views import APIView
from .serializers import SnippetSerial, SnippetSerialthoigian
from rest_framework.response import Response
from kiotapi.models import ThoiGian
import Thread
from datetime import date, timedelta


class SnippetList(APIView):
    def get(self, request, format=None):
        snippet = ReQuest.f
        serializer = SnippetSerial(snippet, many=True)
        return Response(serializer.data)


class Snippetthoigian(APIView):
    def get(self, request, format=None):
        snippet = ThoiGian.objects.all()
        serializer = SnippetSerialthoigian(snippet, many=True)
        return Response(serializer.data)


class IndexView(View):
    def get(self, request):
        danhsach = ReQuest.f
        return render(request, "index.html", {'DS': danhsach})

    def post(self, request):
        checklist = request.POST.getlist('checklist')
        thismonthname = request.POST.getlist('thismonthname')
        if thismonthname == ["true"]:
            starttime = date.today()
            endtime = date.today() + timedelta(days=1)
            ThoiGian.objects.update_or_create(
                id=1,
                defaults={"ThoiGianBatDau": starttime,
                          "THoiGianKetThuc": endtime,
                          "CheDoTimKiem": True
                          })
        else:
            StartTime = request.POST['StartTime']
            EndTime = request.POST['EndTime']
            ThoiGian.objects.update_or_create(
                id=1,
                defaults={"ThoiGianBatDau": StartTime,
                          "THoiGianKetThuc": EndTime,
                          "CheDoTimKiem": False
                          })
        print(checklist)
        return render(request, "index.html")
