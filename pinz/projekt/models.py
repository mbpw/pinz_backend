# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models
from django.contrib.gis.db import models

# Create your models here.

class Dzielnica(models.Model):
    gid = models.AutoField(primary_key=True)
    teryt = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    geometry = models.PolygonField(srid=2180)

    class Meta:
        verbose_name = "Dzielnica"
        verbose_name_plural = "Dzielnice"

    def __unicode__(self):
        return 0

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=32)

    class Meta:
        verbose_name = "Użytkownik"
        verbose_name_plural = "Użytkownicy"

    def __unicode__(self):
        return 0