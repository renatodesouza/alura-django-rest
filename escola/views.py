from django.shortcuts import render

from escola.models import Estudante, Curso
from escola.serializers import EstudanteSerializer, CursoSerializers

from rest_framework import viewsets


class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializers


