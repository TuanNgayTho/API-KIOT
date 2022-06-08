from django.shortcuts import render
from .models import customers
from django.views import View
from django.http import HttpResponse
from ReQuest import f, starttime, endtime, phieutam, xacnhan, hoanthanh
from rest_framework.views import APIView
from .serializers import SnippetSerial
from rest_framework.response import Response


class SnippetList(APIView):
    def get(self, request, format=None):
        snippet = f
        serializer = SnippetSerial(snippet, many=True)
        return Response(serializer.data)


class IndexView(View):
    def get(self, request):
        # danhsach = customers.objects.all()
        danhsach = f
        return render(request, "index.html", {'DS': danhsach})

    def post(self, request):
        global starttime
        global endtime
        global phieutam
        global xacnhan
        global hoanthanh
        starttime = request.POST['StartTime']
        endtime = request.POST['EndTime']
        phieutam = request.POST['PhieuTam']
        xacnhan = request.POST['DaXacNhan']
        hoanthanh = request.POST['HoanThanh']
        return HttpResponse({starttime, endtime, phieutam, xacnhan, hoanthanh})
