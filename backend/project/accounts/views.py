from django.shortcuts import render, get_object_or_404
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

from club.models import Club, Todo
from .models import *
from club.serializers import ClubListSerializers, TodoSerializers
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


# Club 가입자 목록, 가입하기, 탈퇴하기
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def club_regist(request, club_pk):
    user = request.user
    club = get_object_or_404(Club, id=club_pk)
    
    if request.method == 'GET':
        club_serializer = ClubListSerializers(club)
        return Response(club_serializer.data)
    elif request.method == 'POST':
        if user.is_authenticated:
            # 유저가 클럽에 있으면 삭제
            if club.users.filter(id=user.id).exists():
                club.users.remove(user)
            # 유저가 클럽에 없으면 추가
            else:
                club.users.add(user)
            club_serializer = ClubListSerializers(club)
            return Response(club_serializer.data)

# 프로필
@api_view(["GET"])
@permission_classes([AllowAny])
def myprofile(request):
    user = request.user
    print('user:', user)
    if request.method == 'GET':

        # 본인 프로필
        profile = Profile.objects.get(user=user)
        profile_serializer = ProfileSerializer(profile)
        print(profile_serializer.data, '!!!!!!!!!')

        # 유저 클럽 목록
        user_club = Club.objects.filter(users=user)
        # user_club = get_object_or_404(Club, users=user)
        print('user_club:', user_club)
        user_club_list = []
        if user_club:
            for club in user_club:
                print('club:', club)
                club_serializer = ClubListSerializers(club)
                user_club_list.append(club_serializer.data)
            
            
                

        # # 유저 투두리스트 목록
        user_todo = Todo.objects.filter(user=user)
        user_todo_list = []
        if user_todo:
            for todo in user_todo:
                todo_serializer = TodoSerializers(todo)
                user_todo_list.append(todo_serializer.data)




        data = {
            'username':user.username,
            'email':user.email,
            'profile':profile_serializer.data,
            'user_club_list':user_club_list,
            'user_todo_list':user_todo_list

        }

        return Response(data)

# 프로필 수정
@api_view(['GET','PATCH'])
@permission_classes([AllowAny])
def profile_update(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    if request.method == 'GET':
        serializer = ProfileSerializer(profile)

    elif request.method == 'PATCH':
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    data = {
        "profile":serializer.data,
        "username":user.username,
        'email':user.email
    }
    return Response(data)



