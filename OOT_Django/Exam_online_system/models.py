from django.db import models

# Create your models here.
# import the standard Django Model
# from built-in library

# declare a new model with a name "GeeksModel"
class Courses(models.Model):
    name = models.CharField(max_length = 200)    
    title = models.CharField(max_length = 200)
    description = models.TextField()
    Lecturer= models.CharField(max_length = 50)
  
        # renames the instances of the model
        # with their title name
    def __str__(self):
        return self.title
    
class Students(models.Model):
        # fields of the model
    name = models.CharField(max_length = 200)    
    title = models.CharField(max_length = 200)
    Year = models.IntegerField()
    Lecturer= models.CharField(max_length = 50)
    
class Exam(models.Model):
        # fields of the model
    name = models.CharField(max_length = 200)    
    Course = models.CharField(max_length = 200)
    Student = models.IntegerField()
    