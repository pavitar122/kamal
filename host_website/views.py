from django.shortcuts import render
from data import data

# Create your views here.
def host(request):
    value = data
    return render(request,'index.html', {'data':value})