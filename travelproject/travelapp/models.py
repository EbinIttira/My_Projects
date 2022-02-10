from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    def __str__(self):
        return self.name

class Tour_package(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    role= models.TextField(max_length=150)
    def __str__(self):
        return self.name

