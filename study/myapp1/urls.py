from django.urls import path, include 
from .views import HelloAPI, CreateAPI, ViewAPI

urlpatterns = [ 

path("hello/", HelloAPI),
path("create/", CreateAPI),
path("view/", ViewAPI),
]