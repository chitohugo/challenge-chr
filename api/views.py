from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView

from api.models import Station, Network, Project


class StationList(ListView):
    model = Station


class StationDelete(SuccessMessageMixin, DeleteView):
    model = Station
    form = Station
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Station removed !'
        messages.success(self.request, success_message)
        return reverse('list_stations')


class NetworkList(ListView):
    model = Network


class NetworkDelete(SuccessMessageMixin, DeleteView):
    model = Network
    form = Network
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Network removed !'
        messages.success(self.request, success_message)
        return reverse('list_networks')


class ProjectList(ListView):
    model = Project


class ProjectDelete(SuccessMessageMixin, DeleteView):
    model = Project
    form = Project
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Project removed !'
        messages.success(self.request, success_message)
        return reverse('list_projects')
