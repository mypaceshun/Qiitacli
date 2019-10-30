記事用ファイルの作成
====================

記事用のファイルのサンプルは以下の用になります。

.. code-block:: md

   --
   title: Qiita CLI Applicationを作ってみた
   tags:
     - Python
     - Click
   private: yes
   ---
   # ことのはじまり

   Qiitaに記事書きたいけどブラウザ開いていちいちQiitaのエディタ開くのめんどいな〜

   `Vim`使って`MarkDown`で記述してアップロードしたいな〜

   よっしゃ作ったろ！

   # Qiita に記事をアップロードするコマンド

   漠然としたイメージとしては、手頃なテキストエディタで`article.md`のようなファイルを作成し、

   ``` console
   $ qiitacli upload [記事のtitle] article.md
   ```

   と叩いたら記事がアップロードされるイメージ。`Python`と`Click`というモジュールを使ったらできそう。
   なぜ`Python`なのかと言うと私が一番使い慣れているからです。

ファイルの先頭に ``---`` を記述し、次に ``---`` が現れるまでをYAMLヘッダーと認識します。
それ以降は記事本文になりますので、 `Qiita Markdown <https://qiita.com/Qiita/items/c686397e4a0f4f11683d>`_ にかかれている記法で記事を書いてください。

YAMLヘッダー
------------

ファイル先頭に記述するYAMLヘッダーには以下の情報が記述できます。

title
   記事タイトル (必須)

tags
   記事に付けるタグ (1つ以上必須)

private
   限定公開の設定

上記以外の設定は無視されます。
