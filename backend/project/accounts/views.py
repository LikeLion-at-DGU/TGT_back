from asyncore import read
from codecs import raw_unicode_escape_encode
from math import perm
from django.shortcuts import render
from rest_framework.decorators import permission_classes, api_view
from accounts.serializers import *
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django.contrib.auth import authenticate
import jwt
from django.utils import timezone
from datetime import timedelta
from django.conf import settings
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from club.models import Club
from .models import *
from club.serializers import ClubListSerializers
# 회원가입
@api_view(['POST'])
@permission_classes([AllowAny])
def user_regist(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

# 로그인
@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        expired_at = (timezone.now() + timedelta(days=14)).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        access_token = jwt.encode(
            {
                "user_id": user.id,
                "expired_at": expired_at
            },
            settings.SECRET_KEY
        )
        return Response(access_token)
    return Response("Invalid username or password", status=status.HTTP_400_BAD_REQUEST)

# 유저 로그인 확인용
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_login_check(request):
    return Response(request.user.username)



# 프로필
@api_view(["GET"])
@permission_classes([AllowAny])
def myprofile(request):
    user = request.user
    if request.method == 'GET':
        profile = Profile.objects.get(user=user)
        profile_serializer = ProfileSerializer(profile)

        # 유저 클럽 목록
        user_club = Club.objects.filter(user=user)
        user_club_list = []
        if user_club:
            for club in user_club:
                club_serializer = ClubListSerializers(club)
                user_club_list.append(club_serializer.data)
            
                

        # 유저 투두리스트 목록





        data = {
            'profile':profile_serializer,
            'user_club_list':user_club_list,

        }

        return Response(data)

# 프로필 수정
@api_view(['GET','PATCH'])
@permission_classes([AllowAny])
def profile_update(request):
    user = request.user
    if request.method == 'GET':
        profile = Profile.objects.get(user=user)
        serializer = ProfileSerializer(profile)
        return Response(data=serializer.data)
    elif request.method == 'PATCH':
        profile = Profile.objects.get(user=user)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(data=serializer.data)



