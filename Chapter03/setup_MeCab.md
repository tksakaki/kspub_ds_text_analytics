## Linux/WSL

### Ubuntuの場合

```
# mecab のインストール
$ sudo apt install mecab libmecab-dev mecab-ipadic-utf8

# mecab-ipadic-neologdのインストール
$ sudo apt install git curl xz-utils
$ git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
$ cd mecab-ipadic-neologd
$ sudo bin/install-mecab-ipadic-neologd

# python パッケージのインストール
$ sudo apt install swig
$ pip install mecab-python3
```

## CentOSの場合

```
# mecab のインストール
$ sudo yum install --nogpgcheck -y https://packages.groonga.org/centos/groonga-release-
latest.noarch.rpm
$ sudo yum -y install mecab mecab-ipadic mecab-devel patch --nogpgcheck

# mecab-ipadic-neologdのインストール
$ sudo yum install git make curl xz patch 
$ git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
$ cd mecab-ipadic-neologd
$ sudo bin/install-mecab-ipadic-neologd

# python パッケージのインストール
$ sudo yum install swig
$ pip install mecab-python3
```



## MacOS

```
# mecab のインストール
$ brew install mecab
$ brew install mecab-ipadic

# mecab-ipadic-neologd
$ brew install git curl xz
$ git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
$ cd mecab-ipadic-neologd
$ ./bin/install-mecab-ipadic-neologd

# python パッケージのインストール
$ brew install swig
$ pip install mecab-python3
```

