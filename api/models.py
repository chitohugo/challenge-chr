import uuid

from django.contrib.postgres.fields import ArrayField
from django.db import models


class Station(models.Model):
    empty_slots = models.IntegerField()
    extra = models.JSONField(encoder=None)
    free_bikes = models.IntegerField()
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=10, decimal_places=8)
    name = models.CharField(max_length=50)
    timestamp = models.DateTimeField()

    def __str__(self):
        return str(self.name)


class Network(models.Model):
    company = ArrayField(ArrayField(models.CharField(max_length=50)))
    gbfs_href = models.URLField(max_length=200)
    href = models.CharField(max_length=50)
    id = models.CharField(max_length=50, primary_key=True)
    location = models.JSONField(encoder=None)
    name = models.CharField(max_length=50)
    stations = models.ForeignKey(Station, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
