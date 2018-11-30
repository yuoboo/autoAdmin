# encoding=utf8
from .models import Host, Idc
from django import forms
from django.forms.widgets import *


class HostForm(forms.ModelForm):

    class Meta:
        model = Host
        exclude = ('id',)
        widgets = {
            'hostname': TextInput(attrs={'class': 'form-control', 'placeholder': u'必填'}),
            'ip': TextInput(attrs={'class': 'form-control', 'placeholder': u'必填'}),
            'idc': Select(attrs={'class': 'form-control'}),
            'other_ip': TextInput(attrs={'class': 'form-control'}),
            'asset_no': TextInput(attrs={'class': 'form-control'}),
            'asset_type': Select(attrs={'class': 'form-control'}),
            'status': Select(attrs={'class': 'form-control'}),
            'os': TextInput(attrs={'class': 'form-control'}),
            'vendor': TextInput(attrs={'class': 'form-control'}),
            'up_time': DateTimeInput(attrs={'class': 'form-control'}),
            'cpu_model': TextInput(attrs={'class': 'form-control'}),
            'cpu_num': TextInput(attrs={'class': 'form-control'}),
            'memory': TextInput(attrs={'class': 'form-control'}),
            'disk': TextInput(attrs={'class': 'form-control'}),
            'sn': TextInput(attrs={'class': 'form-control'}),
            'position': TextInput(attrs={'class': 'form-control'}),
            'memo': Textarea(attrs={'rows': 4, 'cols': 15, 'class': 'form-control'}),
        }


class IdcForm(forms.ModelForm):

    class Meta:
        model = Idc
        exclude = ('id',)
        widgets = {
            'ids': TextInput(attrs={'class': 'form-control', 'placeholder': u'必填'}),
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': u'必填'}),
            'address': TextInput(attrs={'class': 'form-control'}),
            'tel': TextInput(attrs={'class': 'form-control'}),
            'contact': TextInput(attrs={'class': 'form-control'}),
            'contact_phone': TextInput(attrs={'class': 'form-control'}),
            'jigui': TextInput(attrs={'class': 'form-control'}),
            'ip_range': TextInput(attrs={'class': 'form-control'}),
            'bandwidth': TextInput(attrs={'class': 'form-control'}),
            'memo': Textarea(attrs={'rows': 4, 'cols': 15, 'class': 'form-control'}),
        }
