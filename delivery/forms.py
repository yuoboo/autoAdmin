# encoding=utf8
from django import forms
from delivery.models import AuthInfo, Delivery
from django.forms.widgets import *


class AuthInfoForm(forms.ModelForm):

    class Meta:
        model = AuthInfo
        exclude = ('id',)
        widgets = {
            "dis_name": TextInput(attrs={"class": "form-control", 'placeholder': u'必填'}),
            "username": TextInput(attrs={"class": "form-control"}),
            "password": PasswordInput(attrs={"class": "form-control"}),
            "private_key": Textarea(attrs={'rows': '4', 'cols': '15', "class": "form-control"}),
            "desc": Textarea(attrs={'rows': '2', 'cols': '15', "class": "form-control"}),
        }


class DeliveryForm(forms.ModelForm):

    class Meta:
        model = Delivery
        exclude = ('id', 'status', 'bar_data')
        widgets = {
            'job_name': Select(attrs={'class': 'form-control'}),
            'desc': Textarea(attrs={'rows': '2', 'cols': '15', "class": "form-control"}),
            'deploy_policy': Select(attrs={'class': 'form-control'}),
            'version': TextInput(attrs={'class': 'form-control'}),
            'build_clean': Select(attrs={'class': 'form-control'}, choices=(('True', True), ("False", False))),
            'rsync_del': Select(attrs={'class': 'form-control'}, choices=(('True', True), ("False", False))),
            'shell': TextInput(attrs={'class': 'form-control'}),
            'shell_position': Select(attrs={'class': 'form-control'}, choices=(('True', True), ("False", False))),
            'deploy_num': TextInput(attrs={"class": "form-control"}),
            'auth': Select(attrs={'class': 'form-control'}),
        }
