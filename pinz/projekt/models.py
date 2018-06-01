# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.gis.geos import Point
from django.contrib.gis.geos import Polygon

from .validators import *

# Create your models here.

warszawaPolygon = Polygon(((21.170654296875, 52.07275365395317),
                          (21.170654296875, 52.34624647178617),
                          (20.820465087890625, 52.34624647178617),
                          (20.820465087890625, 52.07275365395317),
                          (21.170654296875, 52.07275365395317)))

class User(AbstractUser):
    points = models.IntegerField(default=0)
    img = models.FileField(default="")

    class Meta:
        verbose_name = "Użytkownik"
        verbose_name_plural = "Użytkownicy"

class Dzielnica(models.Model):
    gid = models.AutoField(primary_key=True)
    teryt = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    geometry = models.PolygonField(srid=4326)

    class Meta:
        verbose_name = "Dzielnica"
        verbose_name_plural = "Dzielnice"

    def __unicode__(self):
        return 0

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    catName = models.CharField(max_length=50)
    icon = models.FileField(blank=True, null=True, upload_to=get_image_folder_cat, validators=[validate_file_extension])

    class Meta:
        verbose_name = "Kategoria typu zgłoszenia"
        verbose_name_plural = "Kategorie typów zgłoszeń"

    def __str__(self):
        return self.catName

    def __unicode__(self):
        return str(self.catName)


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


class ZgloszenieManager(models.Manager):
    def create_zgloszenie(self, type_id, geom, desc, img, user_id):
        print(type_id)
        print(user_id)
        zgl = self.create(geometry=geom, type=type_id, user=user_id)
        zgl.desc = desc
        zgl.img = img
        zgl.save()
        return zgl


class Zgloszenie(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', null=False, related_name="user_id", on_delete=models.CASCADE)
    type = models.ForeignKey('Type', null=True, related_name="type", on_delete=models.PROTECT)
    desc = models.CharField(max_length=255, default="")
    geometry = models.PointField(srid=4326, default=Point(21.010725, 52.220428))
    img = models.FileField(upload_to=get_image_folder_zgl, blank=True, null=True, validators=[validate_file_extension])
    timestamp = models.DateTimeField(auto_now=True)
    fixed = models.BooleanField(default=False)
    objects = ZgloszenieManager()

    class Meta:
        verbose_name = "Zgłoszenie"
        verbose_name_plural = "Zgłoszenia"