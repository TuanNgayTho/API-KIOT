from django.shortcuts import render
from .models import customers
from django.views import View
from django.http import HttpResponse


# Create your views here.

class IndexView(View):
    def get(self, request):
        danhsach = customers.objects.all()
        return render(request, "index.html", {'DS': danhsach})

    def post(self, request):
        data = request.POST['username']
        return HttpResponse({data})
