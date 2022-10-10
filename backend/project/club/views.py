from django.shortcuts import render
from django.urls import is_valid_path
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Club
from .serializers import ClubListSerializers

@api_view(['GET','POST'])
@permission_classes([AllowAny]) # 로그인 된 사람만 볼 수 있음
def club_list_create(request):
    if request.method == 'GET':
        clubs = Club.objects.all()
        serializer = ClubListSerializers(clubs, many=True)

        return Response(data=serializer.data)
    
    if request.method == 'POST':
        serializer = ClubListSerializers(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny]) # 로그인 된 사람만
def club_list(request):
    if request.method == 'GET':
        clubs = Club.objects.all().order_by('-created_at')

