from django.shortcuts import render
from myapp.form import EmpForm
from django.shortcuts import render    
# Create your views here.    
from django.http import HttpResponse, HttpResponseNotFound    
from django.views.decorators.http import require_http_methods    


def index(request):
    return render(request, 'index.html')


def index(request):
    stu = EmpForm()
    return render(request, "index.html", {'form':stu}) 
