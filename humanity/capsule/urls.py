from django.urls import path
from . import views

app_name = 'capsule'

urlpatterns = [
    path('', views.index, name='index'),
    path('journal/', views.journal, name='journal'),
    path('goals/', views.goals, name='goals'),
    path('journal/add_entry/', views.add_entry, name='add_entry'),
    path('notes/', views.notes, name='notes')
]