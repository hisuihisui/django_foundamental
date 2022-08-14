from dataclasses import field

from django import forms

from .models import Friend, Message


class ModelForm(forms.Form):
    name = forms.CharField(
        label="Name", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    mail = forms.EmailField(
        label="Email", widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    gender = forms.BooleanField(
        label="Gender",
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check"}),
    )
    age = forms.IntegerField(
        label="Age", widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    birthday = forms.DateField(
        label="BirthDay(yyyy-mm-dd)",
        widget=forms.DateInput(attrs={"class": "form-control"}),
    )


class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ["name", "mail", "gender", "age", "birthday"]
        # ウィジェットの指定
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "mail": forms.EmailInput(attrs={"class": "form-control"}),
            "age": forms.NumberInput(attrs={"class": "form-control"}),
            "birthday": forms.DateInput(attrs={"class": "form-control"}),
        }


class FindForm(forms.Form):
    find = forms.CharField(
        label="Find",
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )


class CheckForm(forms.Form):
    str = forms.CharField(
        label="String", widget=forms.TextInput(attrs={"class": "form-control"})
    )

    # empty = forms.CharField(
    #     label="Empty",
    #     empty_value=True,
    #     widget=forms.TextInput(attrs={"class": "form-control"})
    # )
    # min = forms.CharField(
    #     label="Min",
    #     min_length=0,
    #     widget=forms.TextInput(attrs={"class": "form-control"})
    # )
    # max = forms.CharField(
    #     label="Max",
    #     max_length=10,
    #     widget=forms.TextInput(attrs={"class": "form-control"})
    # )

    # required = forms.IntegerField(
    #     label='required',
    #     widget=forms.NumberInput(attrs={"class": "form-control"})
    # )
    # min = forms.IntegerField(
    #     label="Min",
    #     min_value=100,
    #     widget=forms.NumberInput(attrs={"class": "form-control"})
    # )
    # max = forms.IntegerField(
    #     label="Max",
    #     max_value=50,
    #     widget=forms.NumberInput(attrs={"class": "form-control"})
    # )

    # date = forms.DateField(
    #     label='Date(dd)',
    #     input_formats=['%d'],
    #     widget=forms.DateInput(attrs={"class": "form-control"})
    # )
    # time = forms.TimeField(
    #     label='Time(HH:MM)',
    #     widget=forms.TimeInput(attrs={"class": "form-control"})
    # )
    # datetime = forms.DateTimeField(
    #     label='DateTime(dd-mm-yyyy)',
    #     widget=forms.DateTimeInput(attrs={"class": "form-control"})
    # )

    # 独自のバリデーション
    def clean(self):
        cleaned_data = super().clean()
        str = cleaned_data["str"]
        if str.lower().startswith("no"):
            raise forms.ValidationError('You input "NO"!')


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["title", "content", "friend"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control form-control-sm"}
            ),
            "content": forms.Textarea(
                attrs={"class": "form-control form-control-sm", "rows": 2}
            ),
            "friend": forms.Select(
                attrs={"class": "form-control form-control-sm"}
            ),
        }
