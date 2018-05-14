# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.gis.geos import Point

# Create your models here.

class User(AbstractUser):
    # email = models.CharField(max_length=100)
    # plec = models.CharField(max_length=1)
    #
    # REQUIRED_FIELDS = ['email']
    # EMAIL_FIELD = 'email'

    class Meta:
        verbose_name = "Użytkownik"
        verbose_name_plural = "Użytkownicy"

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

class Zgloszenie(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(to='Type', on_delete=models.PROTECT)
    geometry = models.PointField(srid=2180, default=Point(660000, 432903))

    class Meta:
        verbose_name = "Zgłoszenie"
        verbose_name_plural = "Zgłoszenia"

class Type(models.Model):
    id = models.AutoField(primary_key=True)
    typeName = models.CharField(max_length=100)
    category = models.ForeignKey(to='Category', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Typ zgłoszenia"
        verbose_name_plural = "Typy zgłoszeń"

    def __str__(self):
        return self.typeName + " [" + str(self.category) + "]"

    def __unicode__(self):
        return str(self.typeName)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    catName = models.CharField(max_length=50)
    icon = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Kategoria typu zgłoszenia"
        verbose_name_plural = "Kategorie typów zgłoszeń"

    def __str__(self):
        return self.catName

    def __unicode__(self):
        return str(self.catName)

# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     password = models.CharField(max_length=32)
#
#     class Meta:
#         verbose_name = "Użytkownik"
#         verbose_name_plural = "Użytkownicy"
#
#     def __unicode__(self):
#         return 0