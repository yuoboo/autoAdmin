# encoding=utf8
from django import forms
from django.contrib import auth
from .models import UserInfo
from django.forms.widgets import *


class LoginUserForm(forms.Form):
    username = forms.CharField(label='账 号', error_messages={'required': u'账号不能为空'},
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='密 码', error_messages={'required': u'密码不能为空'},
                             widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class AddUserForm(forms.ModelForm):

    class Meta:
        model = UserInfo
        fields = ('username', 'password', 'nickname', 'email', 'phonenum','is_active')
        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': u'必填'}),
            'password': PasswordInput(attrs={'class': 'form-control'}),
            'nickname': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': u'必填'}),
            'phonenum': TextInput(attrs={'class': 'form-control', 'placeholder': u'必填'}),
            'is_active': Select(attrs={'class': 'form-control'}, choices=((True, u'启用'), (False, u'禁用'))),

        }

    def __init__(self, *args, **kwargs):
        super(AddUserForm, self).__init__(*args, **kwargs)
        self.fields['is_active'].label = u'状 态'


class EditUserForm(forms.ModelForm):

    class Meta:
        model = UserInfo
        fields = ['username', 'nickname', 'email', 'phonenum', 'is_active']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control', }),
            'nickname': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'phonenum': TextInput(attrs={'class': 'form-control'}),
            'is_active': Select(attrs={'class': 'form-control'}, choices=((True, u'启用'), (False, u'禁用')))
        }

    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].error_messages = {'required': u'请输入账号'}
        self.fields['nickname'].error_messages = {'required': u'请输入姓名'}
        self.fields['email'].error_messages = {'required': u'请输入邮箱', 'invalid': u'请输入有效邮箱'}
        self.fields['phonenum'].error_messages = {'required': u'请输入电话号码'}
        self.fields['is_active'].label = u'状 态'
