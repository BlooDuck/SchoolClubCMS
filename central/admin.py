from django.contrib import admin
from .models import Club, TeamMember, Nav

# Register your models here.
admin.site.register(Club)
admin.site.register(TeamMember)
admin.site.register(Nav)