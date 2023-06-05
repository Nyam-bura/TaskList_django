from django import forms
from Task.models import SubTask,Task


# class SubTaskRegistrationForm(forms.ModelForm):
#     class Meta:
#         model = SubTask
#         fields = "__all__"


class TaskRegistrationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"