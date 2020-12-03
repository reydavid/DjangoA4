from django.urls import path, include
from . import views

app_name = "A4"

urlpatterns = [
    path('', views.index),
    path('display-name', views.name),
    path('display-food', views.food),
    path('display-vacation', views.vacation),
]