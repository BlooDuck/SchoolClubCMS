import imp
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import CreateForm
from .models import Event



def index(request):
    events = Event.objects.all()
    return render(request, 'events/index.html', {"events":events})

def create(request):
    if request.method == "POST":
        form = CreateForm(request.POST) 
        if form.is_valid():
            form.save()
        return redirect(index)
    else:
        form = CreateForm()
        return render(request, 'events/create.html', {"form": form})
