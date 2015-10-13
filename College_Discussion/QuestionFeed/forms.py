from django import forms

class searchform(forms.Form):
    search = forms.CharField(max_length = 300, label='', widget=forms.TextInput())
    