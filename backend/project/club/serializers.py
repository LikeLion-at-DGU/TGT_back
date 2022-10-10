from dataclasses import field
from rest_framework import serializers
from .models import *

class ClubListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
