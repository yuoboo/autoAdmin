# encoding=utf8

from django import forms
from django_celery_beat.models import PeriodicTask, IntervalSchedule, CrontabSchedule


class PeriodicTaskForm(forms.ModelForm):

    class Meta:
        model = PeriodicTask
        exclude = ('id',)


class IntervalForm(forms.ModelForm):

    class Meta:
        model = IntervalSchedule
        exclude = ('id',)


class CrontabForm(forms.ModelForm):

    class Meta:
        model = CrontabSchedule
        exclude = ('id', )
