from django.db import models
from django.db.models.signals import post_save


class Person(models.Model):
    gender_choices = [
        ('male', 'мужской'),
        ('female', 'женский')
    ]

    month_choices = [
        (None, "неизвестен"),
        (1, "Январь"),
        (2, "Февраль"),
        (3, "Март"),
        (4, "Апрель"),
        (5, "Май"),
        (6, "Июнь"),
        (7, "Июль"),
        (8, "Август"),
        (9, "Сентябрь"),
        (10, "Октябрь"),
        (11, "Ноябрь"),
        (12, "Декабрь")
    ]

    name = models.CharField("Имя", max_length=300)
    surname = models.ForeignKey('Surname', verbose_name="Фамилия", on_delete=models.CASCADE, related_name="persons")
    ex_surnames = models.ManyToManyField('Surname', verbose_name="Прошлые фамилии", blank=True,
                                         related_name="ex_persons")
    patronymic = models.CharField("Отчество", max_length=300, null=True, blank=True)
    gender = models.CharField("Пол", max_length=10, choices=gender_choices)

    birth_location = models.ForeignKey('Location', verbose_name="Место рождения", on_delete=models.SET_NULL, null=True,
                                       blank=True, related_name='persons_born')
    year_of_birth = models.IntegerField("Год рождения", null=True, blank=True)
    month_of_birth = models.PositiveSmallIntegerField("Месяц рождения", choices=month_choices, null=True, blank=True)
    day_of_birth = models.PositiveSmallIntegerField("День рождения", null=True, blank=True)

    burial_location = models.ForeignKey('Location', verbose_name="Место захоронения", on_delete=models.SET_NULL,
                                        null=True, blank=True, related_name='persons_buried')
    year_of_death = models.IntegerField("Год смерти", null=True, blank=True)
    month_of_death = models.PositiveSmallIntegerField("Месяц смерти", choices=month_choices, null=True, blank=True)
    day_of_death = models.PositiveSmallIntegerField("День смерти", null=True, blank=True)

    living_locations = models.ManyToManyField('Location', verbose_name="Места жительства", blank=True,
                                              related_name='persons_living')

    additional_information = models.TextField("Дополнительная информация", null=True, blank=True)

    mother = models.ForeignKey('Person', verbose_name="Мать", on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='kids_mother')
    father = models.ForeignKey('Person', verbose_name="Отец", on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='kids_father')
    spouse = models.ForeignKey('self', verbose_name="Супруг(-а)", on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='spouse_reverse')
    ex_spouses = models.ManyToManyField('Person', verbose_name="Бывшие супруги", blank=True,
                                        related_name='ex_spouses_reverse')

    photo = models.ImageField("Фото", upload_to="persons/", null=True, blank=True)

    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Персона"
        verbose_name_plural = "Персоны"

    def get_kids(self):
        return (*self.kids_mother.all(), *self.kids_father.all())

    def __str__(self):
        full_name = ""
        if self.gender == "male":
            full_name += self.surname.male_form
        else:
            full_name += self.surname.female_form
        full_name += " " + self.name
        if self.patronymic is not None:
            full_name += " " + self.patronymic

        return full_name

    def after_save(self):
        if self.spouse is not None:
            spouse_person = Person.objects.get(pk=self.spouse.id)
            if spouse_person.spouse != self:
                spouse_person.spouse = self
                spouse_person.save()
        else:
            try:
                spouse_person = Person.objects.get(spouse=self)
                spouse_person.spouse = None
                spouse_person.save()
            except Exception:
                pass


class Location(models.Model):
    name = models.CharField("Название", max_length=500, unique=True)
    description = models.TextField("Описание", null=True, blank=True)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.name


class Surname(models.Model):
    male_form = models.CharField("Мужская форма", max_length=300)
    female_form = models.CharField("Женская форма", max_length=300)

    class Meta:
        verbose_name = "Фамилия"
        verbose_name_plural = "Фамилии"

    def __str__(self):
        return f"{self.male_form} / {self.female_form}"


def person_saved(sender, instance, *args, **kwargs):
    instance.after_save()


post_save.connect(person_saved, sender=Person)
