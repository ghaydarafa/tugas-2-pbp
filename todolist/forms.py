from django import forms

class CreateTaskForm(forms.Form):
    title = forms.CharField(label='Task Title', max_length=100)
    description = forms.CharField(widget=forms.Textarea)