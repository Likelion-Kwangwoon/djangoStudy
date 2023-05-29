from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import mymodel

from rest_framework.generics import get_object_or_404 
from .serializer import myappSerializer

@api_view(['GET'])
def HelloAPI(request):
    return Response("hello world")

@api_view(['POST'])
def CreateAPI(request):
    serializer = myappSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("success")
    else:
        return Response(serializer.errors , status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def ViewAPI(request):
    board = mymodel.objects.all()
    serializer = myappSerializer(board,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
