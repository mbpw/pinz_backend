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


