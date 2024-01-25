from email.policy import default
from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

import time
from datetime import datetime

class RegisteredUser(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, null=True)
    phone_number = models.CharField(max_length=12)
    def __str__(self):
        return self.name
    
    

class Event(models.Model):
    name = models.CharField(max_length=200)
    
    description = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    registration_deadline = models.DateTimeField(null=True)
    updated = models.DateTimeField(auto_now=True)
    location = models.CharField(null=True,max_length=100)
    participant = models.ManyToManyField(RegisteredUser,blank=True)  
   


   



    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-end_date']

    @property
    def event_status(self):
        status = None
        
        present = datetime.now().timestamp()
        deadline = self.registration_deadline.timestamp()
        past_deadline = (present > deadline)

        if past_deadline:
            status = 'Finished'
        else:
            status = 'Ongoing'

        return status
    
    



    
   


    


