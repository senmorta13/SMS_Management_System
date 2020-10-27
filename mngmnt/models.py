from django.db import models

class Customer(models.Model):
    phnum = models.CharField(max_length=60)    

class Group(models.Model):
    cusl=[Customer()]*10000

class Data_Set(models.Model):
    grol=[Group()]*100





