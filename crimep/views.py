from django.shortcuts import render

from .models import Category,Log

# Create your views here.

def index(request):
    return render(request,'crimep/index.html')

def log(request):
    context = {
        'logs': Log.objects.all()
    }
    return render(request, 'crimep/log.html', context)
