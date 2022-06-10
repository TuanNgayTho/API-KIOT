from django.shortcuts import render
from .models import customers
from django.views import View
from django.http import HttpResponse

import ReQuest
from rest_framework.views import APIView
from .serializers import SnippetSerial
from rest_framework.response import Response
import Thread


class SnippetList(APIView):
    def get(self, request, format=None):
        snippet = ReQuest.f
        serializer = SnippetSerial(snippet, many=True)
        return Response(serializer.data)


class IndexView(View):
    def get(self, request):
        # danhsach = customers.objects.all()
        danhsach = ReQuest.f
        return render(request, "index.html", {'DS': danhsach})

    def post(self, request):
        checklist = request.POST.getlist('checklist')
        ReQuest.starttime = request.POST['StartTime']
        ReQuest.endtime = request.POST['EndTime']
        print(checklist)
        return render(request, "index.html")
        # return HttpResponse({starttime, endtime, checklist})


