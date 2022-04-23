from django.shortcuts import render
from central.models import Club
from django.shortcuts import get_object_or_404, render

def index(request):
    club = Club.objects.filter(name__startswith='School')
    context = {'club':club}
    return render(request, 'index.html', context)

