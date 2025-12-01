from rest_framework import serializers
from .models import User  #we import the User model that we created in models.py

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  #specifying the model to be serialized/ which we want to transform
        fields = '__all__'  #indicating that all fields of the User model should be included in the serialization
        