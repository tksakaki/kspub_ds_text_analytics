# 実践Data Scienceシリーズ Pythonではじめるテキストアナリティクス入門
## 概要

*   このリポジトリは、[講談社サイエンティフィク 実践Data Scienceシリーズ](https://www.kspub.co.jp/book/series/S069.html)の[Pythonではじめるテキストアナリティクス入門](https://www.kspub.co.jp/book/detail/5274101.html) で使用しているコードをまとめたリポジトリです。

*   書籍内の4章、6〜8章、9章〜11章で使用したコードを，Jupyter Notebook形式でまとめなおして公開しています．書籍を読みながら，インタラクティブに実行して頂くことを想定しています．

*   書籍の補助教材としてご活用下さい。

    

## 活用方法

1.   書籍の第3章 環境構築を参照しながら、下記を実行してください。
     *   Pythonのインストール([Chapter03/setup_python.md](Chapter03/setup_python.md) )
     *   Python仮想環境の構築([Chapter03/setup_pyenv.md](Chapter03/setup_pyenv.md))
     *   MeCabのインストール([Chapter03/setup_MeCab.md](Chapter03/setup_MeCab.md) )
         *   書籍ではMeCabのインストールは9章で紹介されていますが，GiNZAでは不向きな処理のために随所でMeCabを利用しているため、最初にインストールするようにしてください．
2.   Jupyter Notebookが実行可能な環境をセットアップしてください。下記は書籍に準拠した場合のセットアップ方法です。

```
pyenv local 3.9.5
pip install jupterlab
```

3.   本リポジトリをダウンロードし、Jupter Notebookが実行可能な環境を立ち上げて下さい。
     *   jupyter-lab以外にJupyter-notebookやVisual Studio Codeなどでも利用可能です

```
$ git clone git@github.com:tksakaki/kspub_ds_text_analytics.git
$ cd kspub_ds_text_analytics
$ jupyter-lab 
```

#### 補足

*   本リポジトリは第4章のコードから順番に実行していくことを想定しています。そのため、順不同で実行すると、Pythonのパッケージが不足することがあります。順番を気にせず実行したい方は、下記のコマンドで利用する全パッケージを予めインストールしてください。

```
$ cd kspub_ds_text_analytics
$ pip install -r requirements.txt
```

## 注意点

*   書籍に記載されている結果は、可能な限り多くの環境で同一の結果が出るように努めていますが、OS/Linuxパッケージ/Pythonパッケージの組み合わせにより、一致しないことは十分に起き得ます。多少の相違はご容赦下さい。

    *   極力合わせたい方は、下記のようのPythonパッケージを最初にインストールすることをおすすめします

        *   ```
            $ pip install -r requirements.txt
            ```

*   第2部 6、8章のコードには、ご自身でデータを収集しないと動かないコードが含まれています。お手数をおかけしますが、幅広く読まれる書籍という性質上、ご理解頂けると幸いです（8章については、ご自身で簡単にデータを収集するコードが含まれています）。

## その他

*   [正誤表（2022年3月10日版）](Others/a_list_of_errata.pdf)
    *   本書籍の最新の正誤表を掲載しています
*   [よくあるトラブルについて](Others/Troubleshooting.md)
    *   環境構築やサンプルプログラム利用時でよくあるトラブルについてまとめています
*   [SudachiPyのバージョン0.5.xと0.6.xについて](Others/SudachiPy.md)
    *   **本書のコードはSudachiPy 0.5.xで動作させることを想定しています**
    *   SudachiPyの0.6.xは0.5.xと比較して分析速度が30倍です
