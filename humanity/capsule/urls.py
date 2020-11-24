from django.urls import path
from . import views

app_name = 'capsule'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('journal/', views.journal, name='journal'),
    path('journal/<int:entry_id>/', views.view_entry, name='view_entry'),
    path('goals/', views.goals, name='goals'),
    path('journal/add_entry/', views.add_entry, name='add_entry'),
    path('notes/', views.notes, name='notes')
]