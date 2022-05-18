from django.contrib import admin

# Register your models here.
    
# Register your models here. 
from .models import course 
    
admin.site.register(course)

# Reister lecturers
from .models import  lecturers 
    
admin.site.register( lecturers) 


#Register 

from .models import  student
    
admin.site.register( student) 