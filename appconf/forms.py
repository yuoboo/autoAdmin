# encoding=utf8

from .models import AppOwner, Product, Project
from django import forms
from django.forms.widgets import *


class ProjectForm(forms.ModelForm):
    '''
    项目表单
    '''
    class Meta:
        model = Project
        exclude = ('id',)
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': u'必填'}),
            'language_type': Select(attrs={'class': 'form-control'}),
            'app_type': Select(attrs={'class': 'form-control'}),
            'server_type': Select(attrs={'class': 'form-control'}),
            'app_arch': Select(attrs={'class': 'form-control'}),
            'source_type': Select(attrs={'class': 'form-control'}),
            'source_address': TextInput(attrs={'class': 'form-control'}),
            'appPath': TextInput(attrs={'class': 'form-control'}),
            'configPath': TextInput(attrs={'class': 'form-control'}),
            'product': Select(attrs={'class': 'form-control'}),
            'owner': Select(attrs={'class': 'form-control'}),
            'serverList': SelectMultiple(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'rows': 4, 'cols': 15, 'class': 'form-control'}),
        }


class AppOwnerForm(forms.ModelForm):
    '''
    负责人表单
    '''
    class Meta:
        model = AppOwner
        exclude = ('id',)
        widgets = {
            'name': TextInput({'class': 'form-control', 'placeholder': u'必填'}),
            'phone': TextInput({'class': 'form-control'}),
            'email': TextInput({'class': 'form-control'}),
            'weChat': TextInput({'class': 'form-control'}),
        }


class ProductForm(forms.ModelForm):
    '''
    产品线表单
    '''
    class Meta:
        model = Product
        exclude = ('id',)
        widgets = {
            'name': TextInput({'class': 'form-control', 'placeholder': u'必填'}),
            'owner': Select({'class': 'form-control'}),
            'description': Textarea({'class': 'form-control'}),
        }
