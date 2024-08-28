from django.shortcuts import render

from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializers, MatriculaSerializer

from rest_framework import viewsets


class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializers

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
