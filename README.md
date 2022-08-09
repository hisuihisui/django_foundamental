# django_fundamental
Python Django 3超入門 学習用リポジトリ<br>
https://www.amazon.co.jp/gp/product/B08CTVCCQ3/ref=ppx_yo_dt_b_d_asin_title_o09?ie=UTF8&psc=1

## メモ
### 2章
### ビュー=コントローラー？
MVCモデル<br>
M = Model      : データアクセス系の処理<br>
V = View       : 画面表示<br>
C = Controller : その他の処理<br>
↓<br>
MVTモデル（Django）<br>
MVCモデルと呼び名が違うだけで、考え方はいっしょ<br>
M = Model      : データアクセス系の処理<br>
V = View       : その他の処理<br>
T = Template   : 画面表示<br>
<br>
### テンプレート
Webページの中に様々な変数などの情報を組み込んだもの<br>
　→　変数に値を代入するなどしてクライアントへ表示<br>
<br>
### なぜtemplatesフォルダ内にアプリケーション名のフォルダが必要か？
Djangoはtemplatesフォルダからの相対パスで検索する<br>
　→　例えば、複数のアプリでtemplates直下にindex.htmlをおくと、パスの区別がつかなくなる<br>
<br>
### Formクラス
前回の入力値を保持しておく<br>
　→　Formクラスを使用する<br>
