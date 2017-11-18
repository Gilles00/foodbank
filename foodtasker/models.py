from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Restaurant(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='restaurant')
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.TimeField()
    logo = models.ImageField(upload_to='restaurant_logo/', blank=False)

    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    avatar = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address= models.TextField()

    def __str__(self):
        return self.user.get_full_name()















