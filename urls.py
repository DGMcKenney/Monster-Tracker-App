from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('get_monsters/', views.get_monsters, name='monsters'),
    path('get_sightings/', views.get_sightings, name='sightings'),
    path('monster_details/<int:id>', views.monster_details, name='monster_details'),
    path('sighting_details/<int:id>', views.sighting_details, name='sighting_details'),
    path('new_monster/', views.new_monster, name='new_monster'),
    path('new_sighting/', views.new_sighting, name='new_sighting'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage')
]