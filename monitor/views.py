from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from .models import Device, PingLog
from .utils import ping_device, send_alert_email
from .forms import DeviceForm

def dashboard(request):
    devices = Device.objects.all()
    online = devices.filter(status='online').count()
    offline = devices.filter(status='offline').count()
    unknown = devices.filter(status='unknown').count()
    context = {
        'devices': devices,
        'online': online,
        'offline': offline,
        'unknown': unknown,
        'total': devices.count(),
    }
    return render(request, 'dashboard.html', context)

def check_device(request, pk):
    device = get_object_or_404(Device, pk=pk)
    result = ping_device(device.ip_address)
    was_offline = device.status == 'offline'
    device.status = result['status']
    device.response_time = result['response_time']
    device.last_checked = timezone.now()
    device.save()
    PingLog.objects.create(
        device=device,
        status=result['status'],
        response_time=result['response_time']
    )
    if result['status'] == 'offline' and not was_offline:
        send_alert_email(device)
    messages.success(request, f"{device.name} is {result['status'].upper()}")
    return redirect('dashboard')

def check_all(request):
    for device in Device.objects.all():
        result = ping_device(device.ip_address)
        was_offline = device.status == 'offline'
        device.status = result['status']
        device.response_time = result['response_time']
        device.last_checked = timezone.now()
        device.save()
        PingLog.objects.create(device=device, status=result['status'], response_time=result['response_time'])
        if result['status'] == 'offline' and not was_offline:
            send_alert_email(device)
    messages.success(request, "All devices checked!")
    return redirect('dashboard')

def add_device(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Device added successfully!")
            return redirect('dashboard')
    else:
        form = DeviceForm()
    return render(request, 'add_device.html', {'form': form})

def device_detail(request, pk):
    device = get_object_or_404(Device, pk=pk)
    logs = device.logs.all()[:50]
    return render(request, 'device_detail.html', {'device': device, 'logs': logs})

def delete_device(request, pk):
    device = get_object_or_404(Device, pk=pk)
    device.delete()
    messages.success(request, "Device deleted!")
    return redirect('dashboard')