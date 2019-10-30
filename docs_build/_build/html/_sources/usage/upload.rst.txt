記事の投稿
==============

記事の投稿には ``upload`` サブコマンドを用います。

::

   $ qiitacli upload --help
   Usage: qiitacli upload [OPTIONS] ARTICLE

     Upload new article

   Options:
     -f, --force  Force upload article
     -T, --tweet  Tweet when article upload[Require Twitter linkage settnigs]
     --help       Show this message and exit.


オプション無しで実行するとアクセストークンで認証しているユーザー記事を投稿します。

::

   $ qiitacli upload article/qiitacli.md
   Are you sure you want to upload? [y/N]: y
   status code: 201


--tweet オプションを追加すると、Qiitaのアカウントに連携しているTwitterのアカウントで記事が投稿されたことをつぶやきます。
これを利用するにはQiitaのアカウントにTwitterのアカウントが連携されている必要があります。

::

   $ qiitacli upload --tweet article/qiitacli.md
   Are you sure you want to upload? [y/N]: y
   status code: 201
