from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home-page'),
    path("anotherpage/", views.another, name='extra-page')
] 