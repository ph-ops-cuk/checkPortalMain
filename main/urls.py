from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('beta/', views.beta, name="beta"),
    path('report/', views.report, name="report"),
    path('tasks/', views.tasks, name="tasks"),
    path('calendar/', views.calendar, name="calendar"),
    path('check_form/', views.check_create, name="check_form"),
    path('check_update/<str:pk>/', views.check_update, name="check_update"),
]
