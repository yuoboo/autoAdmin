# encoding=utf8

from django import forms
from django_celery_beat.models import PeriodicTask, IntervalSchedule, CrontabSchedule
from django.forms.widgets import *


class PeriodicTaskForm(forms.ModelForm):

    class Meta:
        model = PeriodicTask
        exclude = ('id',)

        widgets = {
            'name': TextInput(attrs={"class": "form-control"}),
            'task': TextInput(attrs={"class": "form-control"}),
            'interval': Select(attrs={"class": "form-control"}),
            'crontab': Select(attrs={"class": "form-control"}),
            'solar': Select(attrs={"class": "form-control"}),
            'args': Textarea(attrs={'rows': 1, 'cols': 15, "class": "form-control"}),
            'kwargs': Textarea(attrs={'rows': 1, 'cols': 15, "class": "form-control"}),
            'queue': TextInput(attrs={"class": "form-control"}),
            'exchange': TextInput(attrs={"class": "form-control"}),
            'routing_key': TextInput(attrs={"class": "form-control"}),
            'expires': TextInput(attrs={"class": "form-control"}),
            'enabled': Select(attrs={"class": "form-control"}, choices=((True, "True"), (False, "False"))),
            'description': Textarea(attrs={'rows': 4, 'cols': 15, "class": "form-control"}),
        }


class IntervalForm(forms.ModelForm):

    class Meta:
        model = IntervalSchedule
        exclude = ('id',)


class CrontabForm(forms.ModelForm):

    class Meta:
        model = CrontabSchedule
        exclude = ('id', )
