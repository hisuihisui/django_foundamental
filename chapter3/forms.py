from django import forms

class ModelForm(forms.Form):
    id = forms.IntegerField(label='id')
