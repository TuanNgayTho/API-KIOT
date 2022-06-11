from django.shortcuts import render
from django.views import View
import ReQuest
from rest_framework.views import APIView
from .serializers import SnippetSerial, SnippetSerialthoigian
from rest_framework.response import Response
from kiotapi.models import ThoiGian
import Thread


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
        ReQuest.starttime = request.POST['StartTime']
        ReQuest.endtime = request.POST['EndTime']
        print(checklist)
        return render(request, "index.html")
