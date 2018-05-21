"""pinz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

from projekt import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login),
    url(r'^logout/$', auth_views.logout),
    #url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^api/auth/login', obtain_jwt_token, name="api-login"),
    url(r'^api/auth/verify', verify_jwt_token, name="api-verify"),
    url(r'^api/app/', include('projekt.api.urls'), name="api-app-urls")

    #eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6IndlenlyIiwiZXhwIjoxNTI2OTE3MDM3LCJlbWFpbCI6ImVAbWFpbC5jb20ifQ.5viCK9aZiXGro0kJlXhcU6hZFpKrSpWzHrLWN9ZU1RA
    # url(r'^dzielnice/', views.DzielniceList.as_view()),
    # url(r'^zgloszenia/all', views.ZgloszeniaList.as_view()),
    # url(r'^zgloszenie/$', views.ZgloszenieByID.as_view()),
]
