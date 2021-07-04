from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Libro
from .serializers import libroSerializer

@ csrf_exempt
@api_view(['GET','POST'])
def lista_libros(request):
    
    if request.method =='GET':
        libro = Libro.objects.all()
        serializer = libroSerializer( libro, many=true)
        return response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser() .parse(request)
        serializer = libroSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return   response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                   


# Create your views here.
