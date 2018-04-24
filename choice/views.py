from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Tiku
# Create your views here.

def index(request):
    tm=Tiku.objects.all()
    return render(request,'choice/xz.html',{'tm':tm})


#     return HttpResponse('ok')