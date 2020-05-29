from django import forms

from .models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name',
                  'surname',
                  'patronymic',
                  'gender',

                  'photo',

                  'birth_location',
                  'year_of_birth',
                  'month_of_birth',
                  'day_of_birth',

                  'burial_location',
                  'year_of_death',
                  'month_of_death',
                  'day_of_death',

                  'spouse',
                  'mother',
                  'father',

                  'additional_information',
                  'living_locations',
                  'ex_spouses',
                  'ex_surnames'
                  ]
