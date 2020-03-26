from django.db import models

# Create your models here.

#general information
class GeneralInfo(models.Model):
    logo = models.ImageField()
    email = models.EmailField(max_length=40)
    phoneNumber = models.IntegerField()
    about = models.TextField(max_length=None)

#images model
class ShowImages(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(max_length=1000000)
    image = models.ImageField()

    def __str__(self):
        return self.name

# Management models
class Management(models.Model):
    title=models.CharField(max_length=40)
    name=models.CharField(max_length=40)
    phoneNumber=models.IntegerField()
    email=models.EmailField(max_length=40)
    image=models.ImageField()

    def __str__(self):
        return self.name

# Team model
class Team(models.Model):
    title = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    age=models.IntegerField()
    phoneNumber = models.IntegerField()
    email = models.EmailField(max_length=40)
    image = models.ImageField()

    def __str__(self):
        return self.name

# News
class News(models.Model):
    image=models.ImageField()
    title=models.CharField(max_length=40)
    Story=models.TextField(max_length=10000000)

    def __str__(self):
        return self.title

# Donations
class Donations(models.Model):
    name = models.CharField(max_length=40)
    phoneNumber = models.IntegerField()
    email = models.EmailField(max_length=40)
    amount=models.IntegerField()
    date=models.DateTimeField(max_length=100)

    def __str__(self):
        return self.name

# Supporters
class Support(models.Model):
    image=models.ImageField()
    name = models.CharField(max_length=40)
    phoneNumber = models.IntegerField()
    email = models.EmailField(max_length=40)
    messsage= models.TextField(max_length=10000000)

    def __str__(self):
        return self.name