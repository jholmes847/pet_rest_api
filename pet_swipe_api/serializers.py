from rest_framework import serializers 
from .models import Animal 

class AnimalSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Animal 
        fields = ('id', 'img',  'name', 'age', 'breed', 'color', 'location') 