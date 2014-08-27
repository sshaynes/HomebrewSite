from django.db import models
from django.contrib.auth.models import User
import HomebrewSite

# Create your models here.

class Profiles(models.Model):
    user = models.OneToOneField(User)
    age = models.IntegerField()
    location = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    yearsExperience = models.IntegerField()
    avatarURL = models.CharField(max_length=5000)

class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

class Recipes(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(HomebrewUsers)
    category = models.ForeignKey(Categories)
    description = models.CharField(max_length=5000)

class Conversations(models.Model):
    id = models.AutoField(primary_key=True)
    started = models.DateTimeField()

class UsersFollowing(models.Model):
    id = models.AutoField(primary_key=True)
    followingUser = models.ForeignKey(HomebrewUsers, related_name='followingUser')
    followedUser = models.ForeignKey(HomebrewUsers, related_name='followedUser')
    
class RecipeReviews(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(HomebrewUsers)
    text = models.TextField()
    rating = models.IntegerField()
    
class RecipeSteps(models.Model):
    id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey(Recipes)
    time = models.DateTimeField()
    text = models.TextField(max_length=5000)
    
class RecipeAttributes(models.Model):
    id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey(Recipes)
    name = models.TextField()
    
class Units(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=50)
    abbreviation = models.TextField(max_length=10)
    
class Vendors(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=500)
    url = models.TextField(max_length=5000)
    location = models.TextField(max_length=5000)
    
class VendorReviews(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(HomebrewUsers)
    vendor = models.ForeignKey(Vendors)
    rating = models.IntegerField()
    description = models.TextField(max_length=5000)
    
class Ingredients(models.Model):
    id = models.AutoField(primary_key=True)
    vendor = models.ForeignKey(Vendors)
    name = models.TextField(max_length=500)
    description = models.TextField(max_length=5000)
    
class IngredientAttributes(models.Model):
    id = models.AutoField(primary_key=True)
    ingredient = models.ForeignKey(Ingredients)
    name = models.TextField()

class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(HomebrewUsers)
    text = models.TextField()

class Messages(models.Model):
    id = models.AutoField(primary_key=True)
    authorUser = models.ForeignKey(HomebrewUsers)
    conversation = models.ForeignKey(Conversations)

class UsersConversations(models.Model):
    id = models.AutoField(primary_key=True)
    conversation = models.ForeignKey(Conversations)
    user = models.ForeignKey(HomebrewUsers)
    joined = models.DateTimeField()

class News(models.Model):
    id = models.AutoField(primary_key=True)
    authorUser = models.ForeignKey(HomebrewUsers)
    text = models.TextField(max_length=5000)
    date = models.DateTimeField()
    location = models.TextField(max_length=5000)
    
class IngredientsReviews(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(HomebrewUsers)
    ingredient = models.ForeignKey(Ingredients)
    text = models.TextField(max_length=5000)
    
class RecipeIngredients(models.Model):
    id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey(Recipes)
    ingredient = models.ForeignKey(Ingredients)
    unit = models.ForeignKey(Units)
    quantity = models.DecimalField(decimal_places=2,max_digits=6)