# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Dzielnica
from .models import Zgloszenie
from .api.serializers import DzielnicaSerializer
from .api.serializers import ZgloszenieSerializer

from django.core.serializers import serialize

# Create your views here.

class DzielniceList(APIView):

    def get(self, request):
        dzielnice = Dzielnica.objects.all()
        serializer = DzielnicaSerializer(dzielnice, many=True)
        return Response(serializer.data)

    def post(self):

        pass

class ZgloszeniaList(APIView):

    def get(self, request):
        zgloszenia = Zgloszenie.objects.all()
        serializer = ZgloszenieSerializer(zgloszenia, many=True)
        return Response(serializer.data)
        #data = serialize('geojson', Zgloszenie.objects.all(), geometry_field='geometry')
        #return Response(data)

    def post(self):
        pass

class ZgloszenieByID(APIView):

    def get(self, request):

        params = request.query_params

        if params is not None:
            print(params['id'])
           # data =

        return Response()