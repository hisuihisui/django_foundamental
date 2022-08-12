from django import forms

from .models import Friend


class ModelForm(forms.Form):
    name = forms.CharField(label='Name',\
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    mail = forms.EmailField(label='Email',\
        widget=forms.EmailInput(attrs={'class': 'form-control'}))
    gender = forms.BooleanField(label='Gender',\
        required=False, \
        widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    age = forms.IntegerField(label='Age',\
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    birthday = forms.DateField(label='BirthDay(yyyy-mm-dd)',\
        widget=forms.DateInput(attrs={'class': 'form-control'}))

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name', 'mail', 'gender', 'age', 'birthday']
