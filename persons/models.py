from django.db import models


class Person(models.Model):
    gender_choices = [
        ('male', 'male'),
        ('female', 'female')
    ]

    name = models.CharField(max_length=300)
    surname = models.CharField(max_length=300)
    patronymic = models.CharField(max_length=300, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=gender_choices)

    birth_location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True, blank=True, related_name='persons_born')
    year_of_birth = models.IntegerField(null=True, blank=True)
    month_of_birth = models.PositiveSmallIntegerField(null=True, blank=True)
    day_of_birth = models.PositiveSmallIntegerField(null=True, blank=True)

    burial_location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True, blank=True, related_name='persons_buried')
    year_of_death = models.IntegerField(null=True, blank=True)
    month_of_death = models.PositiveSmallIntegerField(null=True, blank=True)
    day_of_death = models.PositiveSmallIntegerField(null=True, blank=True)

    living_locations = models.ManyToManyField('Location', null=True, blank=True, related_name='persons_living')

    additional_information = models.TextField(null=True, blank=True)

    mother = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True, blank=True, related_name='kids_mother')
    father = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True, blank=True, related_name='kids_father')
    spouse = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='spouse_reverse')

    photo = models.ImageField(upload_to="persons/", null=True, blank=True)

    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Location(models.Model):
    name = models.CharField(max_length=500, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
