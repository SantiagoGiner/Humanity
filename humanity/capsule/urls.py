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
    path('journal/<int:entry_id>/<str:action>/', views.view_entry, name='change_entry'),
    path('goals/', views.goals, name='goals'),
    path('goals/<str:priority>/', views.view_goal, name='view_goal'),
    path('goals/<int:goal_id>/<str:action>/', views.change_goal, name='change_goal'), 
    path('projects/', views.projects, name='projects'),
    path('projects/<int:project_id>/', views.view_project, name='view_project'),
    path('projects/<int:project_id>/<str:action>/', views.change_project, name='change_project'),
    path('projects/<int:project_id>/<int:log_id>', views.view_log, name='view_log')
]