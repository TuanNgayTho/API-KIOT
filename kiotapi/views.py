from django.shortcuts import render
from .models import customers
# Create your views here.

def index(request):
     danhsach = customers.objects.all()
     return render(request, "index.html", {'DS': danhsach})