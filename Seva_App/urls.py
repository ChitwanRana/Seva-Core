from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="index"),
    path('getMatches/', views.get_matches, name="get_matches"),
    path('predict/', views.predict, name="predict"),
]
