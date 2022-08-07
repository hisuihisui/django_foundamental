# クライアント側へレスポンスを返す内容を管理するクラス
from django.http import HttpResponse
from django.shortcuts import render


# request:HttpRequestというクライアント側の情報をまとめたクラス
def index_before(request):
    # クエリパラメータがあるかチェック
    if 'msg' in request.GET:
        # クエリパラメータの取得
        # GETプロパティ -> QueryDictクラス：クエリパラメータを辞書のような形で管理するクラス
        msg = request.GET["msg"]
        result = 'you typed: "' + msg + '".'
    else:
        result = 'please send msg parameter!'

    return HttpResponse(result)

def index(request, id, nickname):
    result = 'your id: ' + str(id) + ', name: "' + nickname +'".'
    return HttpResponse(result)
