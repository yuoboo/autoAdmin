# encoding=utf8
from django import forms
from django_celery_beat.models import PeriodicTask, IntervalSchedule, CrontabSchedule
from django_celery_results.models import TaskResult
from django.forms.widgets import Select
from django.utils.translation import ugettext_lazy as _
from setup import tasks
from celery import current_app
from celery.utils import cached_property
from kombu.utils.json import loads
try:
    from django.utils.encoding import force_text
except ImportError:
    from django.utils.encoding import force_unicode as force_text  # noqa


class TaskSelectWidget(Select):
    """Widget that lets you choose between task names."""

    celery_app = current_app
    _choices = None

    def tasks_as_choices(self):
        _ = self._modules  # noqa
        tasks = list(sorted(name for name in self.celery_app.tasks
                            if not name.startswith('celery.')))
        return (('', ''), ) + tuple(zip(tasks, tasks))

    @property
    def choices(self):
        if self._choices is None:
            self._choices = self.tasks_as_choices()
        return self._choices

    @choices.setter
    def choices(self, _):
        # ChoiceField.__init__ sets ``self.choices = choices``
        # which would override ours.
        pass

    @cached_property
    def _modules(self):
        self.celery_app.loader.import_default_modules()


class TaskChoiceField(forms.ChoiceField):
    """Field that lets you choose between task names."""

    widget = TaskSelectWidget

    def valid_value(self, value):
        return True


class PeriodicTaskForm(forms.ModelForm):

    regtask = TaskChoiceField(
        label=_('Task (registered)'),
        required=False,
    )

    task = forms.CharField(
        label=_('Task (custom)'),
        required=False,
        max_length=200,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    kwargs = forms.CharField(
        label=_(u'任务指令'),
        required=True,
        max_length=200,
        initial='{}',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': u'{"host":"hostname","name":"scritps or command"}'})
    )

    class Meta:
        model = PeriodicTask
        exclude = ('id',)
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control", "placeholder": u"必填"}),
            # 'task': forms.TextInput(attrs={"class": "form-control"}),
            'interval': Select(attrs={"class": "form-control"}),
            'crontab': Select(attrs={"class": "form-control"}),
            'solar': Select(attrs={"class": "form-control"}),
            'args': forms.TextInput(attrs={"class": "form-control", "placeholder": u'默认'}),
            # 'kwargs': forms.TextInput(attrs={'class': 'form-control',
            #                           'placeholder': u'{"host":"your_hostname","name":"scritps_name or command"}'}),
            'queue': forms.TextInput(attrs={"class": "form-control"}),
            'exchange': forms.TextInput(attrs={"class": "form-control"}),
            'routing_key': forms.TextInput(attrs={"class": "form-control"}),
            'expires': forms.TextInput(attrs={"class": "form-control"}),
            'enabled': Select(attrs={"class": "form-control"}, choices=((True, "True"), (False, "False"))),
            'description': forms.Textarea(attrs={'rows': 3, 'cols': 15, "class": "form-control"}),
        }

    def clean(self):
        data = super(PeriodicTaskForm, self).clean()
        regtask = data.get('regtask')
        if regtask:
            data['task'] = regtask
        if not data['task']:
            exc = forms.ValidationError(_('Need name of task'))
            self._errors['task'] = self.error_class(exc.messages)
            raise exc
        return data

    def _clean_json(self, field):
        value = self.cleaned_data[field]
        try:
            loads(value)
        except ValueError as exc:
            raise forms.ValidationError(
                _('Unable to parse JSON: %s') % exc,
            )
        return value

    def clean_args(self):
        return self._clean_json('args')

    def clean_kwargs(self):
        return self._clean_json('kwargs')


class IntervalForm(forms.ModelForm):

    class Meta:
        model = IntervalSchedule
        exclude = ('id',)


class CrontabForm(forms.ModelForm):

    class Meta:
        model = CrontabSchedule
        exclude = ('id', )


class TaskResultForm(forms.ModelForm):

    class Meta:
        model = TaskResult
        exclude = ('id',)