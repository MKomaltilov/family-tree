from django.urls import path

from . import views


app_name = 'persons'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:person_id>/', views.get_person, name="get_person"),
    path('add/', views.add_person, name="add_person")
]