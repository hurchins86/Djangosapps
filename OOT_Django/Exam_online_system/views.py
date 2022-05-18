from django.shortcuts import render


#create your views here

from django.http import HttpResponse

def index(request):
    return HttpResponse('Welcome to KCU!')

# relative import of forms
from .models import Exam,Students,Courses,Courses
 
def list_view(request):
    #dictionary for initial data with
    #field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = Courses.objects.all()
     
    return render(request, "list_view.html", context)
