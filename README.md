# Python Django 3超入門 学習用リポジトリ
https://www.amazon.co.jp/gp/product/B08CTVCCQ3/ref=ppx_yo_dt_b_d_asin_title_o09?ie=UTF8&psc=1

## メモ
### 1章　Djangoを使ってみよう
### Djangoのインストール
```
pip install django
```
### プロジェクトの作成
```
django-admin startproject <プロジェクト名>
```
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

### 検索
・Managerクラスのインスタンスを使用<br>
　→　<モデル>.objects.filter(フィルターの内容)

### あいまいな検索
・値を含む検索<br>
　項目名__contains = 値<br>
・値で始まるものを検索<br>
　項目名__startswith = 値<br>
・値で終わるものを検索<br>
　項目名__endswith = 値<br>
・大文字小文字を区別しない検索<br>
　項目名__iexact = 値<br>
・大文字小文字を区別しないあいまいな検索<br>
　項目名__icontains = 値<br>
　項目名__istartswith = 値<br>
　項目名__iendswith = 値<br>

### 数値の比較
・等しい<br>
　項目名 = 値<br>
・より大きい<br>
　項目名__gt = 値<br>
・以上<br>
　項目名__gte = 値<br>
・より小さい<br>
　項目名__lt = 値<br>
・以下<br>
　項目名__lte = 値<br>

### 複数条件検索
・論理積(AND)<br>
　1. <モデル>.objects.filter(1条件目, 2条件目, ....)<br>
　2. <モデル>.objects.filter(1条件目).filter(2条件目)<br>
・論理和(OR)<br>
　<モデル>.objects.filter( Q(1条件目) | Q(2条件目) ....)<br>

### リストを使った検索
<モデル>.objects.filter(項目名__in=list)<br>


### 4章 データベースをさらに極める
### レコードの並び替え
・昇順<br>
<モデル>.objects.<allやget,filterなど>.order_by(項目名)
<br>
・降順<br>
<モデル>.objects.<allやget,filterなど>.order_by(項目名).reverse()
<br>

### レコードの集計
変数 = <モデル>.objects.aggregate(関数)<br>
　→　辞書型で返ってくるため、「項目名__関数名」で値を取り出す<br>

### クエリの実行
・変数 = <モデル>.objects.raw(クエリ)<br>
・テーブル名：アプリ名_モデル名

### ページネーション
・インスタンスの作成<br>
　変数 = Paginator(コレクション, 1ページあたりのレコード数)
<br>
　　→　コレクション：多数の値をまとめたもの（リストやセット、辞書、QuerySetなど）
<br>
・指定したページのレコードを取り出す<br>
　変数 = <<Paginatorクラス>>.get_page(番号)
<br>
　　→　ページは1からスタートする、Pageというクラスで返ってくる（リストやセットと同じように扱える）

