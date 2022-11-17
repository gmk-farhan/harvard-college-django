from django.shortcuts import render
from .models import groups

def index(request):
    allgroups = groups.objects.all()
    return render(request,'home.html',{groups: allgroups})

def about(request):
    return render(request,'about.html')
