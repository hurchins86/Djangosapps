from django.db import models

# Create your models here.
class course(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    lecturers= models.TextField()
    students = models.TextField()
    
# renames the instances of the model
# with their title name

def __str__(self):
    return self.title
    
    
    
class lecturers(models.Model):
    name=models.CharField(max_length = 200)
    Age=models.CharField(max_length = 200)
    Gender=models.CharField(max_length = 200)
    title=models.CharField(max_length = 200)
    faculty=models.CharField(max_length = 200)
                
class student (models.Model):
    name=models.CharField(max_length = 200)
    Age=models.CharField(max_length = 200)
    Gender=models.CharField(max_length = 200)
    faculty=models.CharField(max_length = 200)