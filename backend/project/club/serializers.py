from rest_framework import serializers
from .models import *

class ClubListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'
        