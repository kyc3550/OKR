from django.shortcuts import render

# Create your views here.

def directions(request):
    return render(request, "directions/direction.html")