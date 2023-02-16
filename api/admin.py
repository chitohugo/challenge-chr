from django.contrib import admin

from .models import Station, Network


class StationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'extra', 'empty_slots', 'free_bikes', 'latitude', 'longitude', 'timestamp')
    search_fields = ('name',)
    ordering = ('-name',)


class NetworkAdmin(admin.ModelAdmin):
    list_display = ('company', 'gbfs_href', 'id', 'href', 'location', 'name')
    search_fields = ('company',)
    ordering = ('-company',)


admin.site.register(Station, StationAdmin)
admin.site.register(Network, NetworkAdmin)
