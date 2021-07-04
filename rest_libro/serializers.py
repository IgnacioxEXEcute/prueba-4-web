from rest_framework import serializers
from core.models import Libro
class libroSerializer(serializers.ModelSerializer):
    class meta:
        model = Libro
        fields = ['ISBN','nombreLibro','autor','Descripcion','categoria']
    
