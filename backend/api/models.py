from __future__ import unicode_literals

from django.db import models
from django.core.validators import *

from django.contrib.auth.models import User, Group

from django.contrib import admin
import base64

class Event(models.Model):
    eventtype = models.CharField(max_length=1000, blank=False)
    timestamp = models.DateTimeField()
    userid = models.CharField(max_length=1000, blank=True)
    requestor = models.GenericIPAddressField(blank=False)

    def __str__(self):
        return str(self.eventtype)

class EventAdmin(admin.ModelAdmin):
    list_display = ('eventtype', 'timestamp')

class ApiKey(models.Model):
    owner = models.CharField(max_length=1000, blank=False)
    key = models.CharField(max_length=5000, blank=False)

    def __str__(self):
        return str(self.owner) + str(self.key)

class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ('owner','key')

class Breed(models.Model):
    name = models.CharField(max_length=50)
    TINY = 'T'
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    SZ_CHOICE = [
        (TINY, 'Tiny'),
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
    ]
    size = models.CharField(
        max_length=1,
        choices=SZ_CHOICE,
        default='T',
    )
    friendliness = models.IntegerField(default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)])
    trainability = models.IntegerField(default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)])
    sheddingamount = models.IntegerField(default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)])
    exerciseneeds = models.IntegerField(default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)])

class Dog(models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(1)])
    age = models.IntegerField(default=1,
        validators=[MinValueValidator(0), MaxValueValidator(30)])
    breed = models.ForeignKey(Breed, default=1,
        verbose_name="Breed", on_delete=models.SET_DEFAULT)
    MALE = 'M'
    FEMALE = 'F'
    GEN_CHOICE = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    gender = models.CharField(
        max_length=1,
        choices=GEN_CHOICE,
        default='U',
    )
    color = models.CharField(max_length=50, validators=[MinLengthValidator(3)])
    favoritefood = models.CharField(max_length=50, default='')
    favoritetoy = models.CharField(max_length=50, default='')
