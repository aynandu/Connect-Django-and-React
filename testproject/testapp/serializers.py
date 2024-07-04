from rest_framework import serializers
from .models import Mymodel

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mymodel
        fields=('id','name','address','mob')