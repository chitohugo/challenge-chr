import uuid

from django.contrib.postgres.fields import ArrayField
from django.db import models


class Station(models.Model):
    empty_slots = models.IntegerField()
    extra = models.JSONField(encoder=None)
    free_bikes = models.IntegerField()
    uid = models.UUIDField(
        default=uuid.uuid4,
        editable=False)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=10, decimal_places=8)
    name = models.CharField(max_length=50)
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return str(self.name)


class Network(models.Model):
    company = ArrayField(ArrayField(models.CharField(max_length=50)))
    gbfs_href = models.URLField(max_length=200)
    href = models.CharField(max_length=50)
    location = models.JSONField(encoder=None)
    name = models.CharField(max_length=50)
    stations = models.ForeignKey(Station, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return str(self.name)


class Project(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    typology = models.CharField(max_length=200)
    holder = models.CharField(max_length=200)
    investment = models.CharField(max_length=200)
    date_admission = models.DateField()
    status = models.CharField(max_length=200)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return str(self.name)
