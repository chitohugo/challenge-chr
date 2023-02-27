import uuid

from django.contrib.postgres.fields import ArrayField
from django.db import models


class BaseAbstract(models.Model):
    name = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['-name']


class Network(BaseAbstract):
    company = ArrayField(ArrayField(models.CharField(max_length=50)))
    gbfs_href = models.URLField(max_length=200)
    href = models.CharField(max_length=50)
    location = models.JSONField(encoder=None)


class Station(BaseAbstract):
    empty_slots = models.IntegerField()
    extra = models.JSONField(encoder=None)
    free_bikes = models.IntegerField()
    uid = models.UUIDField(
        default=uuid.uuid4,
        editable=False)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=10, decimal_places=8)
    timestamp = models.DateTimeField()
    network = models.ForeignKey(Network, on_delete=models.CASCADE)


class Project(BaseAbstract):
    type = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    typology = models.CharField(max_length=200)
    holder = models.CharField(max_length=200)
    investment = models.CharField(max_length=200)
    date_admission = models.DateField()
    status = models.CharField(max_length=200)

