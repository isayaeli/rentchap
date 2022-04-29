from django.urls import path
from .views import home, about, ourApp


urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('ourapp', ourApp, name='ourapp' )
]