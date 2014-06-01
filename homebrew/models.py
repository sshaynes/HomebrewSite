from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class HomebrewUser(User):
    id = models.AutoField(primary_key=True)
    age = models.IntegerField()
    location = models.CharField(max_length=200)
    #name = models.CharField(max-length=200)
    yearsExperience = models.IntegerField
    avatarURL = models.CharField(max_length=2000)

class Category:
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

class Recipe:
    id = models.AutoField(primary_key=True)
    userID = models.ForeignKey(HomebrewUser)
    categoryID = models.ForeignKey(Category)
    description = models.CharField(max_length=2000)