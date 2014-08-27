from django.db import models
from django.contrib.auth.models import User

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
    user = models.ForeignKey(User)
    category = models.ForeignKey(Categories)
    description = models.CharField(max_length=5000)

class Conversations(models.Model):
    id = models.AutoField(primary_key=True)
    started = models.DateTimeField()

class UsersFollowing(models.Model):
    id = models.AutoField(primary_key=True)
    followingUser = models.ForeignKey(User, related_name='followingUser')
    followedUser = models.ForeignKey(User, related_name='followedUser')
    
class RecipeReviews(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
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
    user = models.ForeignKey(User)
    vendor = models.ForeignKey(Vendors)
    rating = models.IntegerField()
    description = models.TextField(max_length=5000)
    
class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    text = models.TextField()

class Messages(models.Model):
    id = models.AutoField(primary_key=True)
    authorUser = models.ForeignKey(User)
    conversation = models.ForeignKey(Conversations)

class UsersConversations(models.Model):
    id = models.AutoField(primary_key=True)
    conversation = models.ForeignKey(Conversations)
    user = models.ForeignKey(User)
    joined = models.DateTimeField()

class News(models.Model):
    id = models.AutoField(primary_key=True)
    authorUser = models.ForeignKey(User)
    text = models.TextField(max_length=5000)
    date = models.DateTimeField()
    location = models.TextField(max_length=5000)
    
#class IngredientsReviews(models.Model):
    #id = models.AutoField(primary_key=True)
    #user = models.ForeignKey(User)
    #ingredient = models.ForeignKey(Ingredients)
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
    vendor = models.ForeignKey(Vendors, null=True)
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
    vendor = models.ForeignKey(Vendors, null=True)
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

class RecipeHops(models.Model):
    id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey(Recipes)
    hop = models.ForeignKey(Hops)
    unit = models.ForeignKey(Units)
    quantity = models.DecimalField(decimal_places=2,max_digits=6)

class RecipeGrains(models.Model):
    id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey(Recipes)
    grain = models.ForeignKey(Grains)
    unit = models.ForeignKey(Units)
    quantity = models.DecimalField(decimal_places=2,max_digits=6)