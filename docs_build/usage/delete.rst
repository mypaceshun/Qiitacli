記事の削除
==========

記事の削除には ``delete`` サブコマンドを用います。

::

   $ qiitacli delete --help
   Usage: qiitacli delete [OPTIONS] ARTICLE_ID

     Delete article

   Options:
     -f, --force  Force delete article
     --help       Show this message and exit.

``delete`` サブコマンドの実行には記事ファイルの他に、削除元の記事のIDが必要になります。
``list`` サブコマンドを用いるなどして記事のIDを確認してください。

::

   $ qiitacli delete xxxxxxxxxxxxxxxxxxxx
   title: Qiita CLI Applicationを作ってみた
   Are you sure you want to delete? [y/N]: y
   status code: 204
