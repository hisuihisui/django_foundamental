# Python Django 3超入門 学習用リポジトリ
https://www.amazon.co.jp/gp/product/B08CTVCCQ3/ref=ppx_yo_dt_b_d_asin_title_o09?ie=UTF8&psc=1

## メモ
### 1章　Djangoを使ってみよう
### Djangoの起動
```
python manage.py runserver
```

### アプリケーションの作成
1. アプリケーションのスタート
```
python manage.py startapp <アプリ名>
```
2. settings.pyに追加<br>
INSTALLED_APPSに登録する<br>

### 2章　ビューとテンプレート
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

### 3章　モデルとデータベース
### Djangoで使用できるデータベース
1. MySQL<br>
　・オープンソースのデータベース<br>
　・サーバータイプ<br>
2. PostgreSQL<br>
　・linuxで広く使用されている<br>
　・サーバータイプ<br>
3. SQLite<br>
　・エンジンタイプ<br>
　　　→　データベースファイルに直接アクセスるタイプ<br>
　・Pythonの標準ライブラリとして組み込まれている<br>

### マイグレーション
・DBの移行を行うための機能<br>
・DBのアップデートにも使われる<br>
<br>
手順
1. マイグレーションファイルの作成
```
python manage.py makemigrations アプリケーション名
```
2. マイグレーションの適用
```
python manage.py migrate
```

### 管理ツール
1. 管理者の作成
```
python manage.py createsuperuser
```
2. モデルの登録<br>
admin.py を編集して登録
3. 管理ツールにログイン<br>
Djangoを起動し、<br>
http://localhost:8000/admin
<br>へアクセスし、ログインする<br>

### Managerクラス
・モデルのobjectsに入っているインスタンスのクラス<br>
・Pythonのメソッドをデータベースクエリに翻訳して実行するもの<br>

### allで得られるのは「QuerySet」クラス
・Setの派生クラス<br>
・クエリ取得用に拡張されている<br>
・valuesメソッド<br>
　1. 取り出したレコードを辞書で返す<br>
　2. 引数に指定した項目名のみ取り出せる（何も指定しなければ、全項目取得）<br>
・values_listメソッド<br>
　1. 取り出したレコードを<b><span style="color: red">タプル</span></b>で返す<br>
　2. 引数に指定した項目名のみ取り出せる（何も指定しなければ、全項目取得）<br>
・firstメソッド<br>
　最初のもののみ返す<br>
・lastメソッド<br>
　最後のもののみ返す<br>
・countメソッド<br>
　取得したレコード数を返す<br>

### メソッドチェーン
・メソッドを次々に呼び出していく書き方<br>
　例) Friends.objects.all().values() <br>

### ModelFormクラス
・本クラスを継承したクラスは内部に「Meta」クラスを作成し、<br>
　modelおよびfieldsを指定する<br>
・継承したクラスの引数に辞書とinstanceにモデルのオブジェクトを指定することで、辞書の値を用いたFormインスタンスを作成できる

### ジェネリックビュー
・指定したモデルの全レコードや特定のIDのもののみを取り出す機能を持った既定のビュークラス<br>
　→コードが少なくなる<br>
1. ListView<br>
・指定したモデルの全レコードを取得する<br>
・テンプレート側に「object_list」で渡す<br>
・「<モデル名>_list.html」というテンプレートを使用する<br>
2. DetailView<br>
・特定のレコードのみ取り出す<br>
　→「pk」というパラメータでプライマリキーを渡す<br>
・テンプレート側に「object」で渡す<br>
・「<モデル名>_detail.html」というテンプレートを使用する<br>
