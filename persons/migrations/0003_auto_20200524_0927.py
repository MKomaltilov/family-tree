# Generated by Django 3.0.6 on 2020-05-24 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0002_auto_20200523_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='ex_surnames',
            field=models.ManyToManyField(blank=True, related_name='ex_persons', to='persons.Surname', verbose_name='Прошлые фамилии'),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(choices=[('male', 'мужской'), ('female', 'женский')], max_length=10, verbose_name='Пол'),
        ),
    ]