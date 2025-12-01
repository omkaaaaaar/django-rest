from rest_framework.decorators import api_view #ts will help us deifne what kinda routes we have
from rest_framework.response import Response  #ts will help us send responses back to the client
from rest_framework import status  #ts will help us send appropriate HTTP status codes
from .models import User  #importing the User model from models.py
from .serializers import UserSerializer  #importing the UserSerializer from serializers.py  

#demo user creation endpoint
#ts below endpoint will return a fake user to check if api is working

@api_view(['GET'])
def get_user(request):
    return Response(UserSerializer({'name': "omkar", "age": 23}))