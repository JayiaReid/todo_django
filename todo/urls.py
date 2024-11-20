from django.urls import path
from . import views

# (5)
urlpatterns = [
    path("", views.home),
    path('list/', views.todo_list, name='todo_list'),
    path('add/', views.add_todo, name='add_todo'),
    path('complete/<int:todo_id>/', views.complete_todo, name='complete_todo'),
]
