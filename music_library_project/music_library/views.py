from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import music_librarySerializer
from .models import Music_library
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.

@api_view(['GET', 'POST'])
def music_library(request):
    
    if request.method == 'GET':
        library = Music_library.objects.all()
        serializer = music_librarySerializer(library, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = music_librarySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def music_details(request, pk):
    song = get_object_or_404(Music_library, pk=pk)
    if request.method == 'GET':
        serializer = music_librarySerializer(song);
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = music_librarySerializer(song, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)