from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

image_address = "static/image"


# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.user.username


class Meal(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    servings = models.IntegerField(default=1)
    preparation_time = models.IntegerField(default=1)
    cooking_time = models.IntegerField(default=1)
    image1 = models.ImageField(upload_to=image_address)
    image2 = models.ImageField(upload_to=image_address)
    image3 = models.ImageField(upload_to=image_address)
    image4 = models.ImageField(upload_to=image_address)
    # image5 = models.ImageField(upload_to=image_address)
    C_level = (
        ('$', '$'),
        ('$$', '$$'),
        ('$$$', '$$$'),
    )
    price_level = models.CharField(max_length=10, choices=C_level, default='text')

    # mood = models.IntegerField(default=1, validators=[MaxValueValidator(4), MinValueValidator(1)])
    vegan = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)

    C_type = (
        ('Snack', 'Snack'),
        ('Break fast', 'Break fast'),
        ('Dinner/Lunch', 'Dinner/Lunch'),
        ('Drink', 'Drink'),
        ('Dessert', 'Dessert'),
    )
    type = models.CharField(max_length=30, choices=C_type, default='text')

    C_mood = (
        ('Happy', 'Happy'),
        ('Bored', 'Bored'),
        ('Sad', 'Sad'),
        ('Angry', 'Angry'),
    )

    mood = models.CharField(max_length=30, choices=C_mood, default='Happy')

    Calories = models.FloatField(default=0)
    Fat = models.FloatField(default=0)
    Carbohydrates = models.FloatField(default=0)
    Protein = models.FloatField(default=0)
    Cholesterol = models.FloatField(default=0)
    Sodium = models.FloatField(default=0)

    def __unicode__(self):
        return self.name


class Ingredient(models.Model):
    meal = models.ForeignKey(Meal, blank=True, null=True)
    text = models.TextField()

    def __unicode__(self):
        return self.meal.name


class Direction(models.Model):
    meal = models.ForeignKey(Meal, blank=True, null=True)
    text = models.TextField()
    order = models.IntegerField(default=1)

    def __unicode__(self):
        return self.meal.name


class Favorite(models.Model):
    meal = models.ForeignKey(Meal, blank=True, null=True)
    profile = models.ForeignKey(Profile, blank=True, null=True)
    is_favorite = models.BooleanField(default=True)

    def __unicode__(self):
        return self.meal.name
