from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class AppUser(models.Model):
    first_name=models.CharField(max_length=100)
    middle_name=models.CharField(max_length=100,blank=True,null=True)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    contact=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    created_at=models.DateTimeField(default=datetime.now())

    class Meta:
        db_table='resumeuser'

    def __str__(self):
        return self.first_name 

class Resume(models.Model):
    province_choice= [
        ('province 1','province 1'),
        ('Madesh','Madesh'),
        ('Bagmati','Bagmati'),
        ('Gandaki','Gandaki'),
        ('Lumbini','Lumbini'),
        ('Karnali','Karnali'),
        ('Sudur Paschim','Sudur Paschim'),
    ]
    name=models.CharField(max_length=100)
    dob=models.DateField(auto_now=False,auto_now_add=False)
    gender=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pin=models.PositiveIntegerField()
    province=models.CharField(choices=province_choice,max_length=50)
    mobile=models.PositiveIntegerField()
    email=models.EmailField()
    job_city=models.CharField(max_length=50)
    profile_image=models.ImageField(upload_to='profileimg',blank=True)
    my_file=models.FileField(upload_to='doc',blank=True)

    class Meta:
        db_table='resumes'        

    def __str__(self):
        return self.name    