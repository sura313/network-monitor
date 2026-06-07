from django.contrib import admin
from .models import Device, PingLog

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'ip_address', 'status', 'response_time', 'last_checked']
    list_filter = ['status']

@admin.register(PingLog)
class PingLogAdmin(admin.ModelAdmin):
    list_display = ['device', 'status', 'response_time', 'timestamp']
    list_filter = ['status', 'device']