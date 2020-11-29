from django.db import models
from django.contrib.auth.hashers import make_password

# from django import forms


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField(default=0)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email
    
    def hash_password(self):
        self.password = make_password(self.password)
        self.save()