from django.db import models

# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=32, blank= False, default="Other")
    def __str__(self):
        return self.name

class Event(models.Model):
    # foreign key should be used here once authentication is done. 
    user = models.CharField(max_length=100)
    event_name = models.CharField(max_length=200)
    location =  models.CharField(max_length=256)
    date = models.DateField()
    start_time = models.TimeField(blank=True)
    end_time = models.TimeField(blank=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="Clubs")
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)