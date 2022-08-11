# クライアント側へレスポンスを返す内容を管理するクラス
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import HelloForm


# viewをクラスとして定義する
# TemplateViewクラスを継承
class HelloView(TemplateView):

    def __init__(self):
        self.params = {
            'title': 'Hello',
            'message': 'your data: ',
            'form': HelloForm(),
            'result': None,
        }

    # Getリクエスト
    def get(self, request):
        return render(request, 'hello/index.html', self.params)

    #POSTリクエスト
    def post(self, request):
        message = 'あなたは、<b>' + request.POST['name'] + \
            '(' + request.POST['age'] + \
            ')</b>さんです。<br>メールアドレスは <b>' + request.POST['mail'] + \
            '</b>ですね。'
        self.params['message'] = message
        self.params['form'] = HelloForm(request.POST)
        # チェックボックスの結果
        # ON：'check':ONが入る
        # OFF：何も値無し -> None
        # if ('check' in request.POST):
        #     self.params['result'] = 'Checked!!'
        # else:
        #     self.params['result'] = 'not checked...'
        # chk = request.POST['check_3_select']
        # self.params['result'] = 'you selected : "' + chk + '".'
        # プルダウンの結果
        # ch = request.POST['choice_select']
        # self.params['result'] = 'you selected : "' + ch + '".'
        # 複数の選択値を取得
        ch = request.POST.getlist('choice_selects')
        result = '<ol class="list-group-item"><b>selected: </b>'
        for item in ch:
            result += '<li class="list-group-item>"' + item + '</li>'
        result += '</ol>'
        self.params['result'] = result
        return render(request, 'hello/index.html', self.params)


def index(request):
    # 辞書にまとめてレンダリングできるようにする
    params = {
        "title": "Hello",
        "message": "your data: ",
        "form": HelloForm(),
        "goto": "next"
    }
    # requestmethodでの分岐
    if (request.method == 'POST'):
        params['message'] = '名前: ' + request.POST['name'] + \
            '<br>メール: ' + request.POST['mail'] + \
            '<br>年齢: ' + request.POST['age']
        params['form'] = HelloForm(request.POST)
    # render(HttpRequestクラス, テンプレート, 辞書)
    # 指定したテンプレートを読み込み、レンダリングして返す
    # 戻り値：TemplateResponseクラス
    return render(request, "hello/index.html", params)


def next(request):
    # 辞書にまとめてレンダリングできるようにする
    params = {"title": "Hello/Next", "msg": "これは、もう一つのページです。", "goto": "index"}
    # render(HttpRequestクラス, テンプレート, 辞書)
    # 指定したテンプレートを読み込み、レンダリングして返す
    # 戻り値：TemplateResponseクラス
    return render(request, "hello/index.html", params)


def form(request):
    # POSTでデータを受け取る
    msg = request.POST["msg"]
    params = {
        "title": "Hello/Form",
        "msg": "こんにちは、" + msg + "さん。",
        "goto": "index",
    }
    return render(request, "hello/index.html", params)


# # request:HttpRequestというクライアント側の情報をまとめたクラス
# def index_before(request):
#     # クエリパラメータがあるかチェック
#     if 'msg' in request.GET:
#         # クエリパラメータの取得
#         # GETプロパティ -> QueryDictクラス：クエリパラメータを辞書のような形で管理するクラス
#         msg = request.GET["msg"]
#         result = 'you typed: "' + msg + '".'
#     else:
#         result = 'please send msg parameter!'

#     return HttpResponse(result)

# def index(request, id, nickname):
#     result = 'your id: ' + str(id) + ', name: "' + nickname +'".'
#     return HttpResponse(result)
