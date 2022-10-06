from django import forms
from .models import Task
class CreateTaskForm(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder": "Task title", 'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Task description", 'class':'form-control'}))

    class Meta:
        model = Task
        fields = ['title', 'description']