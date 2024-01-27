
from django.shortcuts import render
import datetime

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods


from django.shortcuts import render
# importing loading from django template
from django.template import loader
# Create your views here.
from django.http import HttpResponse


def index(request):
   template = loader.get_template('index.html')  # getting our template
   # rendering the template in HttpResponse
   name = {
       'student': 'rahul'
   }
   return HttpResponse(template.render(name))
