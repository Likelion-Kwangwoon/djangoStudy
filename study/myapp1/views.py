from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import mymodel

@api_view(['GET'])#get방식   
def HelloAPI(request):
    return Response("hello world")
