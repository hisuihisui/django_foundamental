from tkinter.tix import Select
from django import forms


# forms.Fromクラスを継承
class HelloForm(forms.Form):
    # 変数 = フィールド
    # labelを設定するとフィールドの手前にラベルのテキストが表示される
    # widget：フォームをHTMLタグとして生成, attrsでクラスを指定
    name = forms.CharField(label='name', \
        # 必須項目か？
        # required=True, \
        required=False, \
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    # メールアドレス
    mail = forms.EmailField(label='mail', \
        required=False, \
        widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # 整数型
    age = forms.IntegerField(label='age', \
        required=False, \
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # 浮動小数点型
    age2 = forms.FloatField(label='age2', \
        required=False, \
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # 整数型
    url = forms.URLField(label='url', \
        required=False, \
        widget=forms.URLInput(attrs={'class': 'form-control'}))
    # 日付
    date = forms.DateField(label='date',\
        required=False, \
        widget=forms.DateInput(attrs={'class': 'form-control'}))
    # 時刻
    time = forms.TimeField(label='time',\
        required=False, \
        widget=forms.TimeInput(attrs={'class': 'form-control'}))
    # 日付＋時刻
    datetime = forms.DateTimeField(label='datetime',\
        required=False, \
        widget=forms.DateTimeInput(attrs={'class': 'form-control'}))
    # チェックボックス
    check = forms.BooleanField(required=False)
    # 3択のNullBooleanField
    check_3_select = forms.NullBooleanField(label='check_3_select',\
        required=False)
    # プルダウン
    data = [
        ('one', 'item1'),
        ('two', 'item2'),
        ('three', 'item3')
    ]
    choices = forms.ChoiceField(label='choices',\
        choices=data, \
        required=False)
    # ラジオボタン
    radio_data = [
        ('one', 'radio 1'),
        ('two', 'radio 2'),
        ('three', 'radio 3')
    ]
    choices_radio = forms.ChoiceField(label='radio_button',\
        choices=radio_data, \
        widget=forms.RadioSelect(),\
        required=False)
    # 選択リスト
    ## 単一項目の選択
    select_data = [
        ('one', 'radio 1'),
        ('two', 'radio 2'),
        ('three', 'radio 3'),
        ('four', 'radio 4'),
        ('five', 'radio 5'),
    ]
    choice_select = forms.ChoiceField(label='radio',\
        choices=select_data,\
        widget=forms.Select(attrs={'size': len(select_data)}), \
        required=False)

    ## 複数項目の選択
    choice_selects = forms.MultipleChoiceField(label='radios',\
        choices=select_data,\
        widget=forms.SelectMultiple(attrs={'size': len(select_data) + 1}), \
        required=False)
