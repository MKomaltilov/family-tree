from django.contrib import admin

from .models import Person, Location, Surname


admin.site.register(Location)
admin.site.register(Surname)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_filter = ('surname', 'gender')

    fieldsets = (
        (None, {
            'fields': (('name', 'surname', 'patronymic'), 'gender', 'photo')
        }),
        ('Информация о рождении', {
            'fields': (('day_of_birth', 'month_of_birth', 'year_of_birth'), 'birth_location')
        }),
        ('Информация о смерти', {
            'fields': (('day_of_death', 'month_of_death', 'year_of_death'), 'burial_location')
        }),
        ('Отношения', {
            'fields': (('mother', 'father', 'spouse'),)
        }),
        (None, {
            'fields': ('additional_information', 'living_locations')
        }),
        ('Разное', {
            'fields': ('ex_surnames', 'ex_spouses')
        })
    )

    filter_horizontal = ('ex_surnames', 'ex_spouses', 'living_locations')
