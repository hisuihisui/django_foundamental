# クライアント側へレスポンスを返す内容を管理するクラス
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # 辞書にまとめてレンダリングできるようにする
    params = {
        'title': 'Hello/Index',
        'msg': 'これは、サンプルで作ったページです。',
        'goto': 'next'
    }
    # render(HttpRequestクラス, テンプレート, 辞書)
    # 指定したテンプレートを読み込み、レンダリングして返す
    # 戻り値：TemplateResponseクラス
    return render(request, 'hello/index.html', params)

def next(request):
    # 辞書にまとめてレンダリングできるようにする
    params = {
        'title': 'Hello/Next',
        'msg': 'これは、もう一つのページです。',
        'goto': 'index'
    }
    # render(HttpRequestクラス, テンプレート, 辞書)
    # 指定したテンプレートを読み込み、レンダリングして返す
    # 戻り値：TemplateResponseクラス
    return render(request, 'hello/index.html', params)

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
