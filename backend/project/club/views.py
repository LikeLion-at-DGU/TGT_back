from django.shortcuts import get_object_or_404, render
from django.urls import is_valid_path
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Club, ClubPost, Todo
from .serializers import ClubListSerializers, TodoSerializers, ClubPostSerializers

from django.db.models import Q

@api_view(['GET','POST'])
@permission_classes([AllowAny]) # 로그인 된 사람만 볼 수 있음
def club_list_create(request):
    user = request.user.id

    if request.method == 'GET':
        clubs = Club.objects.filter(~Q(users=user))
        serializer = ClubListSerializers(clubs, many=True)

        return Response(data=serializer.data)
    
    if request.method == 'POST':
        serializer = ClubListSerializers(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data)

@api_view(['GET', 'DELETE'])
@permission_classes([AllowAny]) # 로그인 된 사람만
def club_detail(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    if request.method == 'GET':
        serilaizer = ClubListSerializers(club)
        return Response(serilaizer.data)
    elif request.method == 'DELETE':
        club.delete()
        return Response("Club Delete Success!")
        

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def club_post_create(request, club_id):
    club = get_object_or_404(Club, id=club_id)

    if request.method == 'GET':
        post = ClubPost.objects.filter(club=club)
        serializer = ClubPostSerializers(post, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = ClubPostSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(
                club=club,
                writer=request.user
            )
        return Response(data=serializer.data)
    
@api_view(['GET','PATCH','DELETE'])
@permission_classes([AllowAny])
def club_post_detail(request, club_id, post_id):
    post = get_object_or_404(ClubPost, id=post_id)

    if request.method == 'GET':
        serializer = ClubPostSerializers(post)
        return Response(serializer.data)
    # elif request.method == 'PATCH':

    elif request.method == 'DELETE':
        post.delete()
        return Response("Post Delete Success!")

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
