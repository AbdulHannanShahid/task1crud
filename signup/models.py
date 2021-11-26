from django.db import models
import datetime
import os

class Person(models.Model):
    person_id = models.AutoField
    person_firstname= models.CharField(max_length=50,default='')
    person_lastname= models.CharField(max_length=30,default='')
    person_email= models.EmailField(max_length=30,default='')
    person_password= models.CharField(max_length=30,default='')
    person_gender= models.CharField(max_length=300,default='')
    person_dob= models.DateField()
    person_img= models.ImageField(blank=True, null=True, upload_to='signup/images')
    def __str__(self):
        return self.person_email