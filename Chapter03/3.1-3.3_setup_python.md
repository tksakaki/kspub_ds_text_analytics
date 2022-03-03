##  Linux

```
$ sudo apt update
$ sudo apt install build-essential git
```

## MacOS

```
# C コンパイラのインストール
$ xcode-select --install

# Homebrewのインストール
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/
install.sh)"

# 必要パッケージのインストール
$ brew install coreutils
$ brew link coreutils
```

 

## Windows

###  1. Window Subsystem for Linuxをインストールする

#### Windows10 バージョン2004 以降またはWindows11 の場合

```## PowerShell（管理者）
Windows PowerShell（管理者）
> wsl ―install
```

#### Windows10 バージョン2004 以前

```
# 1. Windowsの機能「Linux用Windowsサブシステム」を有効にする
## PowerShell（管理者）
> dism.exe /online /enable-feature/featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

# 2. WSL2の実行に関する要件を確認する

# 3. Windowsの機能「仮想マシンプラットフォーム」を有効にする
## PowerShell（管理者）
> dism.exe /online /enable-feature/featurename:VirtualMachinePlatform /all /norestart

## 4. Linuxカーネル更新プログラムパッケージをダウンロードする
https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi をダウンロードして実行します 

## 5. WSL2を既定のバージョンとして設定する
## Windows PowerShell
> wsl --set-default-version 2

## 6.選択したLinux ディストリビューションをインストールする
Microsoft Storeを利用する。もしくは、https://aka.ms/wslubuntu2004 からダウンロードして実行する。
```



### 2. WSLの開始

```
## Windows PowerShell
PS C:\Users\Kodansha> wsl 
```



### 3. WSL上のPythonのインストール

```
$ sudo apt update
$ sudo apt install build-essential git
$ sudo apt install libffi-dev libssl-dev zlib1g-dev liblzma-dev libbz2-dev libreadline-dev libsqlite3-dev libopencv-dev tk-dev
```

