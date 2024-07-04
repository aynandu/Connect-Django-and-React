from django.shortcuts import render
from rest_framework import viewsets
from .models import Mymodel
from .serializers import MyModelSerializer
# Create your views here.
class MyModelView(viewsets.ModelViewSet):
    queryset=Mymodel.objects.all()
    serializer_class=MyModelSerializer