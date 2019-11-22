from django.urls import path
from . import views


app_name = 'todo'


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('todo/<str:category>/', views.todo_category, name='todo_category'),
]