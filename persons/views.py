from django.shortcuts import render, redirect

from .models import Person
from .forms import PersonForm


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


def add_person(request):
    if request.method != 'POST':
        form = PersonForm()
    else:
        form = PersonForm(data=request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            if person.spouse is not None:
                spouse = Person.objects.get(pk=person.spouse.id)
                spouse.spouse = person
                spouse.save()
            person.save()
            return redirect('persons:index')

    context = {'form': form}
    return render(request, 'add_person.html', context)
