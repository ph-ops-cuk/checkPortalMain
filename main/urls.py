from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('status', views.status),
    path('report', views.report),

]
