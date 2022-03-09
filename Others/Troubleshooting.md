# よくあるトラブルについて

## 3章

+   M1 Macでpyenvを用いてPythonのインストールができない（MacOS）
    +   Python 3.9.8以降のバージョンをインストールする
        +   3.9.7以前（本書指定の3.9.5含む）のインストールはM1 Macでうまくいかない場合があります

## 4章

*   head/tailコマンドの実行でエラーがでる（MacOS）

    *   ```
        head: illegal line count -- -14
        ```

    *   head/tailコマンドがMacOS標準のものになっている．下記のいずれかで対処可能

        *   GNUのhead/tailをbrewでインストールし，それを呼び出すようにする

        *   ```
            brew install coreutils
            brew link coreutils
            ```

    *   head/tailの代わりにghead/gtailを用いる

*   nlp(text)を実行すると下記のようなエラーが出る（全環境）

    *   ```
        Exception: Tokenization error: Input is too long, it can't be more than 49149 bytes, was 464332
        ```

    *   SudachiPyのバージョンが0.6以上の場合，長い入力文がエラーとなる．SudachiPyのバージョンを指定して再インストールする（もしくは入力テキストを句点や改行などで区切って入力する）

        *   SudacyPyのバージョン確認方法

            *   ```
                !pip freeze|grep SudachiPy
                ```

        *   SudacyPyの再インストールとNotebookの再起動

            *   ```
                !pip install -U SudachiPy==0.5.4
                ```

            *   JupyterLabのメニューから「Kernal => Restart Kernel...」を選択

            *   Notebookを最初から再実行

*   neologdnがインストールできない（全環境）

    *   gccが古い可能性があるので、gccのアップデートとPython環境のインストールを実施する

        ```
        ## MacOSの場合
        brew upgrade gcc
        pip freeze > current_packages.txt
        pyenv uninstall [現在のPython]
        pyenv install [現在のPythonの再インストール]
        pip install -r current_packages.txt
        ```

*   *   
