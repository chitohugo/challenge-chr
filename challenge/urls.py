"""challenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin

from api.views import StationList, NetworkList, ProjectList, StationDelete, NetworkDelete, ProjectDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('station/', StationList.as_view(template_name="stations/index.html"), name='list_stations'),
    path('station/remove/<int:pk>', StationDelete.as_view(), name='remove_station'),
    path('network/', NetworkList.as_view(template_name="networks/index.html"), name='list_networks'),
    path('network/remove/<int:pk>', NetworkDelete.as_view(), name='remove_network'),
    path('project/', ProjectList.as_view(template_name="projects/index.html"), name='list_projects'),
    path('project/remove/<int:pk>', ProjectDelete.as_view(), name='remove_project'),
]
