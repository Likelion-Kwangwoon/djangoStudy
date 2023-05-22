from django.views import View
from django.http import HttpResponse, JsonResponse

def index(request):
    return HttpResponse("Hello, world.")