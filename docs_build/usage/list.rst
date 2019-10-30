記事の一覧取得
==============

記事の一覧取得には ``list`` サブコマンドを用います。

::

   $ qiitacli list --help
   Usage: qiitacli list [OPTIONS]

     List your article

   Options:
     -i, --id              Show with article id
     -d, --date            Show with article update date
     -t, --tags            Show with article tags
     -u, --url             Show with article url
     -s, --separator TEXT  separator
     --help                Show this message and exit.

オプション無しで実行するとアクセストークンで認証しているユーザーの投稿した記事の一覧が出力されます。
1行目がヘッダーで2行目以降が取得した記事のタイトル一覧になります。

::

   $ qiitacli list
   title
   Qiita CLI Application 作ってみた
   ansible 〜つなぐ〜
   pythonアプリケーションをrpmにパッケージング
   specファイル大解剖
   XAMPPでApacheを起動しAndroidから接続
   AndroidStudio2.0をインストールしてみる

.. WARNING::
   ページネーションの処理が未実装なので最新20件までしか表示されません。
   そのうち実装します。

オプションを追加することで、表示される情報の量を増やすことが出来ます。

::

   $ qiitacli list -i    
   id|title
   c3b97c4eee490d662092|Qiita CLI Application 作ってみた
   ab441d26a12489d5fcbd|ansible 〜つなぐ〜
   b1f3786ce0580201a9e1|pythonアプリケーションをrpmにパッケージング
   5067561d6739cc9e5199|specファイル大解剖
   feedced17884d798fbbd|XAMPPでApacheを起動しAndroidから接続
   c489327d525522de5e65|AndroidStudio2.0をインストールしてみる

オプションは複数まとめて追加できます。

::

   $ qiitacli list -idu
   id|date|title|url
   c3b97c4eee490d662092|2019-10-18T19:35:23+09:00|Qiita CLI Application 作ってみた|https://qiita.com/mypaceshun/items/c3b97c4eee490d662092
   ab441d26a12489d5fcbd|2019-02-01T11:37:55+09:00|ansible 〜つなぐ〜|https://qiita.com/mypaceshun/items/ab441d26a12489d5fcbd
   b1f3786ce0580201a9e1|2018-12-16T07:01:55+09:00|pythonアプリケーションをrpmにパッケージング|https://qiita.com/mypaceshun/items/b1f3786ce0580201a9e1
   5067561d6739cc9e5199|2018-12-19T10:58:45+09:00|specファイル大解剖|https://qiita.com/mypaceshun/items/5067561d6739cc9e5199
   feedced17884d798fbbd|2016-03-14T13:03:04+09:00|XAMPPでApacheを起動しAndroidから接続|https://qiita.com/mypaceshun/items/feedced17884d798fbbd
   c489327d525522de5e65|2016-02-15T10:48:32+09:00|AndroidStudio2.0をインストールしてみる|https://qiita.com/mypaceshun/items/c489327d525522de5e65

-sオプションを使うと区切り文字を変更できます。
例えば区切り文字をカンマなどにするとCSVファイルのような形式で出力されます。

::

   $ qiitacli list -idu -s ,
   id,date,title,url
   c3b97c4eee490d662092,2019-10-18T19:35:23+09:00,Qiita CLI Application 作ってみた,https://qiita.com/mypaceshun/items/c3b97c4eee490d662092
   ab441d26a12489d5fcbd,2019-02-01T11:37:55+09:00,ansible 〜つなぐ〜,https://qiita.com/mypaceshun/items/ab441d26a12489d5fcbd
   b1f3786ce0580201a9e1,2018-12-16T07:01:55+09:00,pythonアプリケーションをrpmにパッケージング,https://qiita.com/mypaceshun/items/b1f3786ce0580201a9e1
   5067561d6739cc9e5199,2018-12-19T10:58:45+09:00,specファイル大解剖,https://qiita.com/mypaceshun/items/5067561d6739cc9e5199
   feedced17884d798fbbd,2016-03-14T13:03:04+09:00,XAMPPでApacheを起動しAndroidから接続,https://qiita.com/mypaceshun/items/feedced17884d798fbbd
   c489327d525522de5e65,2016-02-15T10:48:32+09:00,AndroidStudio2.0をインストールしてみる,https://qiita.com/mypaceshun/items/c489327d525522de5e65
