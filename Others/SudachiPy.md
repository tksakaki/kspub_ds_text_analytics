# SudachiPyのバージョン違いについて

本書で利用しているspaCy+GiNZAでは，形態素解析ツールとしてSudachiPyを利用しています．書籍出版日（2022年3月10日）現在，SudachiPyの最新バージョンは0.6.3となっていますが，SudachiPyはバージョン0.5.xと0.6.xで大きく実装が異なっています．具体的には下記のような違いです．

* SudachiPy 0.5.xまでは，Pythonのみで実装されています
  * Pythonが実行できる環境があれば使用可能です
* SudachiPy 0.6.x以降は，Rustで実装されています
  * 0.5.x以前と比べ，分析速度が飛躍的に向上しています（30倍程度高速化したとされています）
  * ただし，使用するためにはRustのインストールが必要です
  * 正式には0.6.x以降はsudachi.rs[https://github.com/WorksApplications/sudachi.rs]と呼ばれます（以下，sudachi.rs）と呼びます）

本書では，執筆当時の最新バージョンであったSudachiPy 0.5.xを使用しています．sudachi.rsでは動作しないコードが含まれています．そのため，プログラムコードを正常動作させたい方には，SudachiPy 0.5.xを推奨しています．

他方，分析速度という点ではsudachi.rsが優れています．7章や8章では分析に時間がかかるプログラムコードもあることから，分析速度を優先する方にはsudachi.rsをおすすめします．ただし，プログラムコードが正しく動作しないことがあるため，その場合は，ご自身でエラーメッセージを見ながらプログラムコードを修正してください．



### sudachi.rsを使用するために

#### Rustのインストール

以下2つのインストール方法があります

* [Rustupの利用](https://www.rust-lang.org/ja/tools/install)（WSL/Linux/MacOS）

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

* Homebrewの利用（MacOSのみ）

```
# rustupインストールおよびrust環境のセットアップ
brew install rustup-init
rustup-init
# シェルの再起動
exec $SHELL -l
```



