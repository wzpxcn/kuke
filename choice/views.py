from django.shortcuts import render
from django.http import HttpResponse
from .models import Tiku
# Create your views here.

def index(request):
    tk_list=Tiku.objects.all()
    return render(request,'choice/xz.html',context={'tk_list':tk_list})


#     return HttpResponse('ok')