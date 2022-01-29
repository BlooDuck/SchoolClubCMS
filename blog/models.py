from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)        # post title
    author = models.CharField(max_length=50)        # post author
    body = models.TextField()                       # post body
    pub_date = models.DateField('date published')   # pub date of post
    

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)        # ties comment to post
    author = models.CharField(max_length=50)                        # comment author
    body = models.TextField()                                       # comment body
    pub_date = models.DateField('date published')                   # comment pub date

    # returns body as class str
    def __str__(self):
        return self.body

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

