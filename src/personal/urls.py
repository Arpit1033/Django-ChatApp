from django.urls import path
from .views import *

urlpatterns = [
    path('', home_screen_view, name='home')
]