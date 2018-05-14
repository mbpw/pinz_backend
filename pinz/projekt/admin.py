# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Dzielnica
from .models import User

# Register your models here.
class DzielnicaAdmin(admin.ModelAdmin):
    list_display = ('gid','name','teryt','geometry')

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','password')

admin.site.register(Dzielnica, DzielnicaAdmin)
admin.site.register(User, UserAdmin)
