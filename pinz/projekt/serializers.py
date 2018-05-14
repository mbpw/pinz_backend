from rest_framework import serializers
from .models import Dzielnica

class DzielnicaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dzielnica
        fields = ('gid','name')
