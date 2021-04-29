from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('beta/', views.betapage, name="beta"),
    path('report/', views.reportpage, name="report"),
    path('tasks/', views.taskpage, name="tasks"),
    path('calendar/', views.calendar, name="calendar"),
    path('check/<str:pk>/', views.checkpage, name="check"),
    path('check_form/', views.create_check, name="check_form"),
    path('check_update/<str:pk>/', views.update_check, name="check_update"),
    path('result_update/<str:pk>/', views.update_result, name="result_update"),
    path('result_create/', views.create_result, name="result_create"),
]
