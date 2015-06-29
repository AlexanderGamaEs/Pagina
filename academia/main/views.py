from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from main.models import SectionMainPage
from main.serializers import SectionMainPageSerializer

class SectionList(generics.ListCreateAPIView):
    queryset = SectionMainPage.objects.all()
    serializer_class = SectionMainPageSerializer

def index(request):
    return render(request, 'main/index.htm')
