from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import AnimalSerializer
from .models import Animal

class AnimalList(generics.ListCreateAPIView):
    queryset = Animal.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = AnimalSerializer # tell django what serializer to use

class AnimalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all().order_by('id')
    serializer_class = AnimalSerializer