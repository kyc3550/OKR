from django.shortcuts import render
from .models import BoxerInfo
# Create your views here.

def boxer_info(reqest):
    context = {}
    context['boxers'] = BoxerInfo.objects.all()
    return render(reqest,'boxer/boxer_info.html',context)