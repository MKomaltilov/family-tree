from django.shortcuts import render

from .models import Person


def index(request):
    persons = Person.objects.all()
    context = {
        'persons': persons
    }
    return render(request, 'index.html', context)
