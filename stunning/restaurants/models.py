# -*- encoding: utf-8 -*-
from django.db import models


class Restaurant(models.Model):
    name = models.CharField("Nombre", max_length=140, unique=True)
    rating = models.IntegerField("Valoración", default=0)
    phone = models.CharField("Teléfono", max_length=15)
    city = models.CharField("Ciudad", max_length=150)

    def __unicode__(self):
        return self.name
