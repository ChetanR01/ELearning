from django.db import models
from datetime import datetime

# Create your models here.
class Registration(models.Model):
    name= models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    UserTypes= [
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('panchayat', 'Panchayat'),
        ('volunteer', 'Volunteer'),    
        ('donator', 'Donator'),    
        ('other', 'Other'),]
    type= models.CharField(max_length=100,choices=UserTypes)
    subject= models.CharField(max_length=500)
    message=models.TextField()
    date=models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name+"("+self.type+")"