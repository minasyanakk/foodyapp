from django.db import models
from django.contrib.auth.models import User


 
class Foods(models.Model):
    title = models.CharField(max_length=400, unique=False)
    gi = models.CharField(max_length=200, unique=False)
    serve = models.CharField(max_length=200, unique=False)
    carb_per_serve = models.CharField(max_length=200, unique=False)
    gl = models.CharField(max_length=200, unique=False)
    class Meta:
        ordering = ['-title']

    def __str__(self):
        return self.title
        

class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    ingredients = models.TextField()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title