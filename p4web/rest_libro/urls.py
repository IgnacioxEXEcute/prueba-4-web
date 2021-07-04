from django.urls import path
from rest_libro.views import lista_libros

urlpatterns = [
    path('lista_libros', lista_libros, name="lista_libros"),
]