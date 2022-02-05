from django.db import models

# Create your models here.

class Club(models.Model):
    about = models.TextField()
    name = models.CharField(max_length=100)

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    pic = models.ImageField(max_length=200)
    title = models.CharField(max_length=100)

class Nav(models.Model):
    item = models.CharField(max_length=50)
    link = models.URLField(max_length=200)