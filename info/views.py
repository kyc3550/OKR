from django.shortcuts import render
from info.models import TimeInfo, PriceInfo, Info
# Create your views here.

def info(request):
    context = {}
    context['infos'] = Info.objects.all()
    context['timeinfos'] = TimeInfo.objects.all()
    context['priceinfos'] = PriceInfo.objects.all()
    return render(request, "info/info.html",context)