from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('Welcome to KCA Online Register!')


from django.shortcuts import render
 
# relative import of forms
from .models import course
 
 
def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = course.objects.all()
         
    return render(request, "list_view.html", context)