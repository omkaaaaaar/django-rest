from django.urls import path
from .views import get_user #importing the get_user view from views.py

urlpattens = [
    path('user/', get_user, name='get_user') #defining the route for the get_user endpoint
]