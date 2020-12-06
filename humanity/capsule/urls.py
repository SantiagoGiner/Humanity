from django.urls import path
from . import views

app_name = 'capsule'

# All the url paths of the application
urlpatterns = [
    # Default route
    path('', views.index, name='index'),
    # Routes to login, logout, register, and delete account
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('delete/', views.delete, name='delete'),

    # Routes related to user's journal
    path('journal/', views.journal, name='journal'),
    path('journal/<int:entry_id>/', views.view_entry, name='view_entry'),
    path('journal/<int:entry_id>/<str:action>/', views.view_entry, name='change_entry'),

    # Routes related to user's goals
    path('goals/', views.goals, name='goals'),
    path('goals/<str:priority>/', views.goals, name='goals'),
    path('goals/<int:goal_id>/<str:action>/', views.change_goal, name='change_goal'),

    # Routes related to user's projects
    path('projects/', views.projects, name='projects'),
    path('projects/<int:project_id>/', views.view_project, name='view_project'),
    path('projects/<int:project_id>/<str:action>/', views.change_project, name='change_project'),
    path('projects/<int:project_id>/<int:log_id>', views.view_log, name='view_log'),

    # Routes related to user's mini time capsules
    path('minicapsule/', views.mini_capsule, name='mini_capsule'),
    path('minicapsule/<int:capsule_id>/', views.view_capsule, name='view_capsule'),

    # Routes related to user's library
    path('library/', views.library, name='library'),
    path('library/<int:book_id>', views.library, name='library'),
    path('library/add_book/', views.add_book, name='add_book'),
    path('library/notes/<int:book_id>/', views.book_notes, name='book_notes'),
    path('library/view_note/<int:note_id>/', views.view_note, name='view_note'),
    path('library/view_note/<int:note_id>/<str:action>', views.view_note, name='view_note')
]