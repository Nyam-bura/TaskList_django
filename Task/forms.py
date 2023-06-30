from django import forms
from Task.models import Task

class TaskRegistrationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"