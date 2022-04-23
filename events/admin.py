from django.contrib import admin
# Register your models here.
from .models import Club, Event

admin.site.register(Club)
admin.site.register(Event)