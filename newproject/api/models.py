from django.db import models

# Create your models here.
class User(models.Model):
    age = models.IntegerField()  #defining age as integer fieldm we are taking only 2 fields
    name = models.CharField(max_length=100) #defining name as character field with max length 100

    def __str__(self): #a special method that determines what is displayed when you call str() on an instance of the mode
        return self.name  #ts will make sure that when we print a User object, it will display the name of the user 
    
#print(User) #ts will return the name of the user instead of a generic object representation
