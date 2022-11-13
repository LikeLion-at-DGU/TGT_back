from dataclasses import field
from rest_framework import serializers
from .models import *

class ClubPostSerializers(serializers.ModelSerializer):

    writer = serializers.PrimaryKeyRelatedField(read_only=True)
    club = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = ClubPost
        fields = '__all__'
        read_only_fields = ('club', )


class ClubListSerializers(serializers.ModelSerializer):

    # users = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Club
        fields = (
            'id',
            'name',
            'introduce',
            'content',
            'image',
            'category',
            'start_date',
            'end_date',
            'howto',
            'created_at',
            'updated_at',
            'users',
        )



class TodoSerializers(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Todo
        fields = '__all__'
