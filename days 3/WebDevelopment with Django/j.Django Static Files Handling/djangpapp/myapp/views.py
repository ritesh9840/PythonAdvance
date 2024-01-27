from django.shortcuts import render    
# Create your views here.    
from django.http import HttpResponse, HttpResponseNotFound    
from django.views.decorators.http import require_http_methods    

def index(request):
    return render(request, 'index.html')
