from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.list import ListView

from api.models import Station, Network, Project


class StationList(ListView):
    paginate_by = 10
    model = Station


class StationUpdate(SuccessMessageMixin, UpdateView):
    model = Station
    form = Station
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Station updated!'
        messages.success(self.request, success_message)
        return reverse('list_stations')


class StationDelete(SuccessMessageMixin, DeleteView):
    model = Station
    form = Station
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Station removed!'
        messages.success(self.request, success_message)
        return reverse('list_stations')


class NetworkList(ListView):
    paginate_by = 10
    model = Network


class NetworkUpdate(SuccessMessageMixin, UpdateView):
    model = Network
    form = Network
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Network updated!'
        messages.success(self.request, success_message)
        return reverse('list_network')


class NetworkDelete(SuccessMessageMixin, DeleteView):
    model = Network
    form = Network
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Network removed!'
        messages.success(self.request, success_message)
        return reverse('list_networks')


class ProjectList(ListView):
    paginate_by = 10
    model = Project


class ProjectUpdate(SuccessMessageMixin, UpdateView):
    model = Project
    form = Project
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Project updated!'
        messages.success(self.request, success_message)
        return reverse('list_projects')


class ProjectDelete(SuccessMessageMixin, DeleteView):
    model = Project
    form = Project
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Project removed!'
        messages.success(self.request, success_message)
        return reverse('list_projects')
