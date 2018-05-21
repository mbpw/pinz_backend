from django.conf.urls import url

from .views import UserAPIView

urlpatterns = [
    url(r'^user/(?P<id>\d+)/$', UserAPIView.as_view(), name='post-rud')
]
