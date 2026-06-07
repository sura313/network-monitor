from django import forms
from .models import Device

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'ip_address', 'description', 'alert_email']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }