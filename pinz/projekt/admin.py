# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Dzielnica
from .models import User
from .models import Zgloszenie
from .models import Type
from .models import Category
from django.contrib.auth.admin import UserAdmin
from django.contrib.gis.admin.options import OSMGeoAdmin
from django.contrib.gis.admin.options import GeoModelAdmin


class WarsawOSMGeoAdmin(OSMGeoAdmin):
    default_lon = 2338980.709696
    default_lat = 6839986.585356
    default_zoom = 12


# Register your models here.
class DzielnicaAdmin(WarsawOSMGeoAdmin):
    list_display = ('gid','name','teryt')


#class UserAdmin(admin.ModelAdmin):
    #list_display = ('id','name','password')


class ZgloszenieAdmin(WarsawOSMGeoAdmin):
    list_display = ('id','type','desc')
    pass


class TypeAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'catName', 'icon')


admin.site.register(Dzielnica, DzielnicaAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Zgloszenie, ZgloszenieAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Category, CategoryAdmin)
