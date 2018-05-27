from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeometrySerializerMethodField
from rest_framework.validators import UniqueValidator

from projekt.models import User
from projekt.models import Dzielnica
from projekt.models import Zgloszenie
from projekt.models import Type
from projekt.models import Category


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, required=True, write_only=True)
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    img = serializers.FileField(required=False)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'img',
            'points'
        ]

    def create(self, validated_data):
        new_user = User.objects.create_user(validated_data['username'], validated_data['email'],
                                        validated_data['password'])

        if 'first_name' in validated_data:
            new_user.first_name = validated_data['first_name']
        if 'last_name' in validated_data:
            new_user.last_name = validated_data['last_name']
        if 'img' in validated_data:
            new_user.img = validated_data['img']

        new_user.save()
        return new_user

    def validate_username(self, value):
        qs = User.objects.filter(username__iexact=value)  # including instance
        if self.instance:
            qs = qs.exclude(id=self.instance.id)
        if qs.exists():
            raise serializers.ValidationError("This username has already been used")
        return value

    def validate_email(self, value):
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
        fields = ('gid', 'name')


class ZgloszenieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Zgloszenie


class ZgloszenieGeoSerializer(GeoFeatureModelSerializer):
    dzielnica = serializers.SerializerMethodField(method_name='getDzielnica')

    class Meta:
        model = Zgloszenie
        geo_field = "geometry"
        depth = 2
        fields = ('type','desc','geometry','dzielnica')

    def getDzielnica(self, zgl):
        sql = Dzielnica.objects.raw(
            "SELECT dz.gid, dz.name FROM projekt_dzielnica dz, projekt_zgloszenie zg WHERE ST_Contains(dz.geometry, zg.geometry) AND zg.id=" + str(
                zgl.id) + ";")
        print(list(sql))
        if list(sql):
            return sql[0].name
        else:
            return "PUNKT NIE ZNAJDUJE SIĘ W WARSZAWIE"


class ZgloszenieSerializer(serializers.ModelSerializer):
    #type = serializers.IntegerField
    dzielnica = serializers.SerializerMethodField(method_name='getDzielnica')
    geometry = serializers.CharField(allow_null=False)

    class Meta:
        model = Zgloszenie
        geo_field = "geometry"
        fields = ('__all__')

    def getDzielnica(self, zgl):
        sql = Dzielnica.objects.raw(
            "SELECT dz.gid, dz.name FROM projekt_dzielnica dz, projekt_zgloszenie zg WHERE ST_Contains(dz.geometry, zg.geometry) AND zg.id=" + str(
                zgl.id) + ";")
        print(list(sql))
        if list(sql):
            return sql[0].name
        else:
            return "PUNKT NIE ZNAJDUJE SIĘ W WARSZAWIE"

    def create(self, validated_data):

        print(validated_data)


        desc = validated_data.get('desc')


        # # Description
        # if 'desc' in validated_data:
        #     desc = validated_data['desc']
        # else:
        #     desc = ""

        # Image
        if 'img' in validated_data:
            img = validated_data['img']
        else:
            img = ""

        zgl = Zgloszenie.objects.create_zgloszenie(validated_data['type'], validated_data['geometry'], desc, img, validated_data['user'])

        return zgl


class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        depth = 1
        fields = ('__all__')


class CategorySerializer(serializers.ModelSerializer):
    nazwa = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Category
        fields = ('nazwa')