from django import forms
from django.forms import widgets
from .models import TaskItem


class NewTaskForm(forms.ModelForm):
    description = forms.CharField(widget=widgets.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'New task...'
                }),
            max_length=100,
            label=''
        )

    class Meta:
        model = TaskItem
        fields = ["description"]
