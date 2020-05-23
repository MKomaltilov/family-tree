from django.contrib import admin

from .models import Person, Location, Surname


admin.site.register(Person)
admin.site.register(Location)
admin.site.register(Surname)