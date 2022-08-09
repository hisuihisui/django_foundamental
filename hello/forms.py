from django import forms


# forms.Fromクラスを継承
class HelloForm(forms.Form):
    # 変数 = フィールド
    # labelを設定するとフィールドの手前にラベルのテキストが表示される
    # widget：フォームをHTMLタグとして生成, attrsでクラスを指定
    name = forms.CharField(label='name', \
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    mail = forms.CharField(label='mail', \
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(label='age', \
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
