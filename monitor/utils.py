import subprocess
import platform
import requests
from datetime import datetime
from django.utils import timezone

def ping_device(ip_address):
    system = platform.system().lower()
    if system == 'windows':
        command = ['ping', '-n', '1', '-w', '2000', ip_address]
    else:
        command = ['ping', '-c', '1', '-W', '2', ip_address]

    try:
        start = timezone.now()
        result = subprocess.run(command, capture_output=True, text=True, timeout=5)
        end = timezone.now()
        response_time = (end - start).total_seconds() * 1000

        if result.returncode == 0:
            return {'status': 'online', 'response_time': round(response_time, 2)}
        else:
            return {'status': 'offline', 'response_time': None}
    except Exception:
        return {'status': 'offline', 'response_time': None}


def send_alert_email(device):
    from django.core.mail import send_mail
    if not device.alert_email:
        return
    send_mail(
        subject=f'[ALERT] {device.name} is OFFLINE',
        message=f'''
Device Alert — Network Monitor

Device: {device.name}
IP Address: {device.ip_address}
Status: OFFLINE
Last Checked: {device.last_checked}

Please check the device immediately.
        ''',
        from_email=None,
        recipient_list=[device.alert_email],
        fail_silently=True,
    )