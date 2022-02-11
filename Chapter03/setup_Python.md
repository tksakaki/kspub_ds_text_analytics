## pyenvのセットアップ

```git clone https://github.com/pyenv/pyenv.git ~/.pyenv
## pyenvのインストール
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv

## .bash_profileへの書き込み
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
$ echo 'eval "$(pyenv init --path)"' >> ~/.bash_profile

## インストール可能なPythonのバージョンの確認
$ pyenv install -l

## Python 3.9.5のインストールと使用するバージョンの指定
$ pyenv install -v 3.9.5
$ pyenv local 3.9.5
```

