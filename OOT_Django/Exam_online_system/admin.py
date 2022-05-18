from django.contrib import admin
    
# Register your models here. 
from .models import (Courses,Students,Exam)
    
admin.site.register(Courses) 
admin.site.register(Students)
admin.site.register(Exam)