from django import forms

class searchform(forms.Form):
    search = forms.CharField(max_length = 300, label='', widget=forms.TextInput(), help_text="Search...")
    
class askquestionform(forms.Form):
    question = forms.CharField(label="", widget = forms.Textarea)
    tags = forms.CharField(label ="", max_length= 100)
    anonymous = forms.BooleanField(label = "")
    
class answerquestionform(forms.Form):
    answer = forms.CharField(label ="", widget = forms.Textarea)
    