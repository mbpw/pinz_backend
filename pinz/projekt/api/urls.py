from django.conf.urls import url

from .views import *
# from .views import UserDetailView
# from .views import UserListView
# from .views import UserRegisterView
# from .views import ZgloszenieAddView
# from .views import DzielniceListView

from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

urlpatterns = [
    url(r'^user/detail/(?P<id>\d+)/$', UserDetailView.as_view(), name='api-user-detail'),
    url(r'^user/list/$', UserListView.as_view(), name='api-user-list'),
    url(r'^user/register/$', UserRegisterView.as_view(), name='api-user-register'),

    url(r'^user/login', obtain_jwt_token, name="api-login"),
    url(r'^user/verify', verify_jwt_token, name="api-verify-token"),
    url(r'^user/refresh', refresh_jwt_token, name="api-refresh-token"),

    url(r'^zgloszenia/add/$', ZgloszenieAddView.as_view(), name='api-zgloszenia-add'),
    url(r'^zgloszenia/list/$', ZgloszenieList.as_view(), name='api-zgloszenia-list'),
    url(r'^zgloszenia/find/$', ZgloszenieByAttributes.as_view(), name='api-zgloszenia-find'),

    url(r'^types/list/$', TypeListView.as_view(), name='api-types-list'),
    url(r'^cats/icons/$', CatIconView.as_view(), name='api-cats-icons'),

    url(r'^dzielnice/list/$', DzielniceListView.as_view(), name='api-dzielnice-list')

]
