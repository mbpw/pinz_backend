from django.db.models import Q
from rest_framework import generics, mixins
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from django.db.models.functions import Coalesce

from datetime import datetime, timedelta

from projekt.models import User
from projekt.models import Zgloszenie
from projekt.models import Dzielnica
from projekt.models import Type
from projekt.models import Category
from rest_framework.views import APIView
from rest_framework.response import Response

from .permissions import IsAdminOrCurrUser
from .serializers import UserSerializer, CatIconSerializer
from .serializers import ZgloszenieSerializer
from .serializers import ZgloszenieGeoSerializer
from .serializers import DzielnicaSerializer
from .serializers import TypeSerializer
from .serializers import CategorySerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated


#
# Użytkownik
#

class UserDetailView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAdminOrCurrUser,)


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)


class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = ()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


#
# Zgłoszenie
#

class ZgloszenieAddView(generics.CreateAPIView):
    serializer_class = ZgloszenieSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ZgloszenieList(APIView):
    queryset = Zgloszenie.objects.all()

    # serializer_class = ZgloszenieSerializer(many=True)

    def get(self, request):
        zgloszenia = Zgloszenie.objects.all()
        serializer = ZgloszenieGeoSerializer(zgloszenia, many=True)
        return Response(serializer.data)


def parseDate(stringDate):
    spl = stringDate.split('-')
    l = len(spl)
    y, M, d, h, m, s = [0, 0, 0, 0, 0, 0]
    if l > 0:
        y = int(spl[0])
    if l > 1:
        M = int(spl[1])
    if l > 2:
        d = int(spl[2])
    if l > 3:
        h = int(spl[3])
    if l > 4:
        m = int(spl[4])
    if l > 5:
        s = int(spl[5])
    return [y, M, d, h, m, s]


class ZgloszenieByAttributes(APIView):

    def get(self, request):
        params = request.query_params
        objects = Zgloszenie.objects.all()

        if params is not None:

            if 'user' in params:
                users = params.get('user')
                usr = [int(s) for s in users.split(',')]
                objects = objects.filter(user__in=usr)

            if 'id' in params:
                ids = params.get('id')
                idd = [int(s) for s in ids.split(',')]
                objects = objects.filter(id__in=idd)

            if 'type' in params:
                types = params.get('type')
                if types is not None:
                    tps = [int(s) for s in types.split(',')]
                    objects = objects.filter(type__in=tps)

            if 'radius' in params and 'lat' in params and 'lon' in params:
                radius = params['radius']
                lon = float(params.get('lon'))
                lat = float(params.get('lat'))
                point = Point(lon, lat)
                objects = objects.filter(geometry__distance_lt=(point, Distance(km=radius)))

            if 'daterange' in params:
                rangesplit = params.get('daterange').split(':')

                if len(rangesplit) == 2:
                    parseDate(rangesplit[0])
                    start_date = datetime(*parseDate(rangesplit[0]))
                    end_date = datetime(*parseDate(rangesplit[1]))
                    objects = objects.filter(timestamp__range=(start_date, end_date))

            if 'date' in params:
                # 2018-06-01-19-23-32
                # YYYY-MM-DD-hh-mm-ss
                spl = params.get('date').split('-')
                l = len(spl)
                if l > 0:
                    objects = objects.filter(timestamp__year=spl[0])
                if l > 1:
                    objects = objects.filter(timestamp__month=spl[1])
                if l > 2:
                    objects = objects.filter(timestamp__day=spl[2])
                if l > 3:
                    objects = objects.filter(timestamp__hour=spl[3])
                if l > 4:
                    objects = objects.filter(timestamp__minute=spl[4])
                if l > 5:
                    objects = objects.filter(timestamp__second=spl[5])

            if 'latest' in params:
                latest = int(params.get('latest'))  # minutes
                threshold = datetime.now() - timedelta(minutes=latest)
                print(threshold)
                objects = objects.filter(timestamp__gte=threshold)

            if 'fixed' in params:
                if params.get('fixed') in ('0', 'false', 'False', 'infixed', 'n', 'N'):
                    objects = objects.filter(fixed=False)
                else:
                    objects = objects.filter(fixed=True)

            if 'order' in params:
                spl = params.get('order').split(',')
                if 'desc' in params:
                    spl = ['-' + s for s in spl]
                    objects = objects.order_by(*spl)
                else:
                    objects = objects.order_by(*spl)

        serializer = ZgloszenieSerializer(objects, many=True)
        return Response(serializer.data)


#
# Dzielnica
#

class DzielniceListView(APIView):
    permission_classes = ()

    def get(self, request):
        dzielnice = Dzielnica.objects.all()
        serializer = DzielnicaSerializer(dzielnice, many=True)
        return Response(serializer.data)

    def post(self):
        pass


#
# Typy zgłoszeń
#

class TypeListView(generics.ListAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    lookup_field = 'id'
    permission_classes = ()


class CatIconView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CatIconSerializer
    permission_classes = ()
    pass