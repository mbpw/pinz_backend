# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Dzielnica
from .serializers import DzielnicaSerializer

# Create your views here.

class DzielniceList(APIView):

    def get(self, request):
        dzielnice = Dzielnica.objects.all()
        serializer = DzielnicaSerializer(dzielnice, many=True)
        return Response(serializer.data)

    def post(self):

        pass

    pass