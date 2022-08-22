from re import A
from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRoutes),

]
