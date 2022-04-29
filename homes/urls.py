from django.urls import path
from .views import homes, single_home

urlpatterns = [
    path('houses', homes, name='homes'),
    path('single-house/<int:id>', single_home,  name='single_home')
]