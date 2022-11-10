from django.shortcuts import get_object_or_404, render
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
        club = get_object_or_404(Club, id=request.data['club'])

        serializer = TodoSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(
                club=club,
                user=request.user
            )
            return Response(serializer.data)
    return Response(serializer.errors)


# 투두리스트 상세, 수정, 삭제
@api_view(['GET','PATCH','DELETE'])
def todolist_detail(request, pk):
    todo = Todo.objects.get(id=pk)

    if request.method == 'GET':
        serializer = TodoSerializers(todo)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        serializer = TodoSerializers(instance=todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        todo.delete()
        return Response("Delete Success")
