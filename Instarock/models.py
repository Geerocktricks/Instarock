from django.db import models
import datetime as dt

#Create your models here
class User(models.Model):
    '''
    Method to create users profile
    '''
    username = models.CharField(max_length =50)
    useremail = models.CharField(max_length = 140)
    userpassword = models.CharField(max_length = 100)
