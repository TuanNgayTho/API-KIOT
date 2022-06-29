from django.shortcuts import render
from django.views import View
import ReQuest
import Thread
from rest_framework.views import APIView
from .serializers import SnippetSerial, SnippetSerialthoigian
from rest_framework.response import Response
from kiotapi.models import ThoiGian
from datetime import date, timedelta


class SnippetList(APIView):
    def get(self, request, format=None):
        snippet = ReQuest.hoanthanh
        serializer = SnippetSerial(snippet, many=True)
        return Response(serializer.data)

class SnippetListxacnhan(APIView):
    def get(self, request, format=None):
        snippet = ReQuest.xacnhan
        serializer = SnippetSerial(snippet, many=True)
        return Response(serializer.data)

class SnippetListphieutam(APIView):
    def get(self, request, format=None):
        snippet = ReQuest.phieutam
        serializer = SnippetSerial(snippet, many=True)
        return Response(serializer.data)

class Snippetthoigian(APIView):
    def get(self, request, format=None):
        snippet = ThoiGian.objects.all()
        serializer = SnippetSerialthoigian(snippet, many=True)
        return Response(serializer.data)


class IndexView(View):
    def get(self, request):
        danhsach = ReQuest.hoanthanh
        return render(request, "index.html", {'DS': danhsach})

    def post(self, request):
        checklist = request.POST.getlist('checklist')
        thismonthname = request.POST.getlist('thismonthname')
        if thismonthname == ["true"]:
            now = date.today()
            monday = now - timedelta(days=now.weekday())
            starttime = monday
            endtime = date.today()
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
