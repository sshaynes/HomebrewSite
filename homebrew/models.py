from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User)
    age = models.IntegerField()
    location = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    yearsExperience = models.IntegerField()
    avatarURL = models.CharField(max_length=5000)

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    description = models.CharField(max_length=5000)

class Conversation(models.Model):
    id = models.AutoField(primary_key=True)
    started = models.DateTimeField()

class UserFollowing(models.Model):
    id = models.AutoField(primary_key=True)
    followingUser = models.ForeignKey(User, related_name='followingUser')
    followedUser = models.ForeignKey(User, related_name='followedUser')
    
class RecipeReview(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    text = models.TextField()
    rating = models.IntegerField()
    
class RecipeStep(models.Model):
    id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey(Recipe)
    time = models.DateTimeField()
    text = models.TextField(max_length=5000)
    
class RecipeAttribute(models.Model):
    id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey(Recipe)
    name = models.TextField()
    
class Unit(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=50)
    abbreviation = models.TextField(max_length=10)
    
class Vendor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=500)
    url = models.TextField(max_length=5000)
    location = models.TextField(max_length=5000)
    
class VendorReview(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    vendor = models.ForeignKey(Vendor)
    rating = models.IntegerField()
    description = models.TextField(max_length=5000)
    
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    text = models.TextField()

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    authorUser = models.ForeignKey(User)
    conversation = models.ForeignKey(Conversation)

class UserConversation(models.Model):
    id = models.AutoField(primary_key=True)
    conversation = models.ForeignKey(Conversation)
    user = models.ForeignKey(User)
    joined = models.DateTimeField()

class New(models.Model):
    id = models.AutoField(primary_key=True)
    authorUser = models.ForeignKey(User)
    text = models.TextField(max_length=5000)
    date = models.DateTimeField()
    location = models.TextField(max_length=5000)
    
#class IngredientReview(models.Model):
    #id = models.AutoField(primary_key=True)
    #user = models.ForeignKey(User)
    #ingredient = models.ForeignKey(Ingredient)
    #text = models.TextField(max_length=5000)

class Hop(models.Model):
    origin = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    notes = models.CharField(max_length=5000)
    alpha = models.CharField(max_length=200)
    amount = models.CharField(max_length=200)
    use = models.CharField(max_length=200)
    displayAmount = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    beta = models.CharField(max_length=200)
    form = models.CharField(max_length=200)
    displayTime = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    hsi = models.CharField(max_length=200)
    vendor = models.ForeignKey(Vendor, null=True)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.name
    
class Grain(models.Model):
    origin = models.CharField(max_length=200, null=True, blank=True, default="")
    recommendMash = models.CharField(max_length=200)
    notes = models.CharField(max_length=5000, null=True, blank=True, default="")
    addAfterBoil = models.CharField(max_length=200)
    amount = models.CharField(max_length=200)
    maxInBatch = models.CharField(max_length=200)
    displayAmount = models.CharField(max_length=200)
    protein = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    supplier = models.CharField(max_length=200, null=True, blank=True, default="")
    displayColor = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    potential = models.CharField(max_length=200)
    moisture = models.CharField(max_length=200)
    coarseFineDiff = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    extractSubstitue = models.CharField(max_length=200, blank=True, null=True, default="")
    diastaticPower = models.CharField(max_length=200)
    ibuGalPerLb = models.CharField(max_length=200)
    yeild = models.CharField(max_length=200)
    vendor = models.ForeignKey(Vendor, null=True)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.name
	
class Yeast(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True, default="")
	type = models.CharField(max_length=200)
	form = models.CharField(max_length=200)
	laboratory = models.CharField(max_length=200)
	amount = models.CharField(max_length=200)
	amount_is_weight = models.CharField(max_length=200)
	product_id = models.CharField(max_length=200)
	min_temperature = models.CharField(max_length=200)
	max_temperature = models.CharField(max_length=200)
	flocculation = models.CharField(max_length=200, null=True, blank=True, default="")
	attenuation = models.CharField(max_length=200)
	notes = models.CharField(max_length=2000, null=True, blank=True, default="")
	best_for = models.CharField(max_length=200)
	times_cultured = models.CharField(max_length=200)
	max_reuse = models.CharField(max_length=200)
	add_to_secondary = models.CharField(max_length=200)
	display_amount = models.CharField(max_length=200, blank=True, null=True, default="")
	disp_min_temp = models.CharField(max_length=200)
	disp_max_temp = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.name

class RecipeHop(models.Model):
    id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey(Recipe)
    hop = models.ForeignKey(Hop)
    unit = models.ForeignKey(Unit)
    quantity = models.DecimalField(decimal_places=2,max_digits=6)

class RecipeGrain(models.Model):
    id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey(Recipe)
    grain = models.ForeignKey(Grain)
    unit = models.ForeignKey(Unit)
    quantity = models.DecimalField(decimal_places=2,max_digits=6)