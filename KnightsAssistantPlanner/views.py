from django.shortcuts import render
from django.http import HttpResponse

# Create your views here
def index (request):
    return render(request, 'index.html')

def newsPage (request):
    return render(request, 'newspage.html')

def myHealth (request):
    return render(request, 'myHealth.html')
