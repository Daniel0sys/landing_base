from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, FileResponse


def index(request):
    return render(request, "index.html")
    # return HttpResponse("Hello, world. You're at the polls index.")