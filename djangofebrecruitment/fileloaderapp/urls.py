from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home-page'),
    path("errorrip/", views.another, name='error-page'),
    path("delete/", views.deleteitem, name='delete-page'),
    path("results/", views.results, name='results-page')
] 