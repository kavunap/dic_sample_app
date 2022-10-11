from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(label='Title',  max_length=100)
    body = forms.CharField(label='Body', widget=forms.Textarea)
