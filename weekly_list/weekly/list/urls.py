from django.urls import path, include
from .import views
from .views import *

urlpatterns = [
   path('add/', views.add_task, name='add_task'),
   path('', views.task_list, name='task_list'),  
]
