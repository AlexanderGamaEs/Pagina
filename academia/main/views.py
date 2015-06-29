from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from main.models import SectionMainPage
from main.serializers import SectionMainPageSerializer

class SectionList(APIView):
    def get(self, request, name, format=None):
        try:
            sections = SectionMainPage.objects.get(name=name)
        except Snippet.DoesNotExist:
            raise Http404 
        serializer = SectionMainPageSerializer(sections, many=True)
        return Response(serializer.data)

    def post(self, request, name, format=None):
        return self.get(self, request, name, format=format)

def index(request):
    return render(request, 'main/index.htm')
