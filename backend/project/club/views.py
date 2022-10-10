from django.shortcuts import render
from django.urls import is_valid_path
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Club
from .serializers import ClubListSerializers

from .models import Todo
from .serializers import TodoSerializers

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



#투두리스트 view

@api_view(["GET", "POST"])
def todo_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializers(todos , many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # todolists = Todo.objects.filter(user=request.data['user_id'])
        # 투두리스트 클래스에 유저 추가 필요 !!
        serializer = TodoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def tododelete(request,pk):
    todo = Todo.objects.get(id = pk)
    todo.delete()
    return Response("Delete Success")

@api_view(["PUT"])
def todoupdate(request,pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializers(todo , data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

