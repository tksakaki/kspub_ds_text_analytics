# よくあるトラブルについて

*   neologdnがインストールできない（MacOSの場合）

    *   brewのgccが古い可能性があるので、gccのアップデートとPython環境のインストールを実施する

        ```
        *   brew upgrade gcc
        *   pip freeze > current_packages.txt
        *   pyenv uninstall [現在のPython]
        *   pyenv install [現在のPythonの再インストール]
        *   pip install -r current_packages.txt
        ```
