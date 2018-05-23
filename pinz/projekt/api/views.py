from django.db.models import Q
from rest_framework import generics, mixins

from projekt.models import User
from projekt.models import Zgloszenie
from projekt.models import Dzielnica
from rest_framework.views import APIView
from rest_framework.response import Response

from .permissions import IsAdminOrCurrUser
from .serializers import UserSerializer
from .serializers import ZgloszenieSerializer
from .serializers import DzielnicaSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated


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

class ZgloszenieAddView(generics.CreateAPIView):
    serializer_class = ZgloszenieSerializer
    #permission_classes = (IsAuthenticated)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class DzielniceListView(APIView):
    permission_classes = ()

    def get(self, request):
        dzielnice = Dzielnica.objects.all()
        serializer = DzielnicaSerializer(dzielnice, many=True)
        return Response(serializer.data)

    def post(self):

        pass