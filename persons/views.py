from django.shortcuts import render

from .models import Person


def index(request):
    persons = Person.objects.all()
    context = {
        'persons': persons
    }
    return render(request, 'index.html', context)


def get_person(request, person_id):
    person = Person.objects.get(id=person_id)
    context = {
        'person': person
    }
    return render(request, 'person.html', context)
