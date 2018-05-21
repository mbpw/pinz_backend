from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from projekt.models import User
from projekt.models import Dzielnica
from projekt.models import Zgloszenie

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
        ]

    def validate_username(self, value):
        qs = User.objects.filter(username__iexact=value)  # including instance
        if self.instance:
            qs = qs.exclude(id=self.instance.id)
        if qs.exists():
            raise serializers.ValidationError("This username has already been used")
        return value

    def validate_username(self, value):
        qs = User.objects.filter(email__iexact=value)  # including instance
        if self.instance:
            qs = qs.exclude(id=self.instance.id)
        if qs.exists():
            raise serializers.ValidationError("This email has already been used")
        return value

class DzielnicaSerializer(serializers.ModelSerializer):

    #lat = serializers.
    class Meta:
        model = Dzielnica
        fields = ('gid','name')

class LoginSerializer(serializers.ModelSerializer):

    pass


class ZgloszenieSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Zgloszenie
        geo_field = "geometry"
        fields = ('__all__')
