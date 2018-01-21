# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Meetups(models.Model):
    Description = models.CharField(max_length=500)
    Date  = models.DateField()
    Time =  models.TimeField()
    Venue = models.CharField(max_length=50)
    Topic = models.CharField(max_length=50)

    def __str__(self):
        return self.Description




