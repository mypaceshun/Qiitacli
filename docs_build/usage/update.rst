記事の更新
==============

記事の更新には ``update`` サブコマンドを用います。

::

   $ qiitacli update --help
   Usage: qiitacli update [OPTIONS] ARTICLE_ID ARTICLE

     Update article

   Options:
     -f, --force  Force update article
     --help       Show this message and exit.

``update`` サブコマンドの実行には記事ファイルの他に、更新元の記事のIDが必要になります。
``list`` サブコマンドを用いるなどして記事のIDを確認してください。

::

   $ qiitacli update xxxxxxxxxxxxxxxxxxxx article/qiitacli.md
   title: [Qiita CLI Applicationを作ってみた]
   articlefile: [article/qiitacli.md]
   Are you sure you want to update? [y/N]: y
   status code: 200
