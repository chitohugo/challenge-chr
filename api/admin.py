from django.contrib import admin

from .models import Station, Network, Project


class StationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'extra', 'empty_slots', 'free_bikes', 'latitude', 'longitude', 'timestamp')
    search_fields = ('name',)
    ordering = ('-name',)


class NetworkAdmin(admin.ModelAdmin):
    list_display = ('company', 'gbfs_href', 'id', 'href', 'location', 'name')
    search_fields = ('company',)
    ordering = ('-company',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'region', 'typology', 'holder', 'investment', 'date_admission', 'status')
    search_fields = ('name',)
    ordering = ('-name',)


admin.site.register(Station, StationAdmin)
admin.site.register(Network, NetworkAdmin)
admin.site.register(Project, ProjectAdmin)
