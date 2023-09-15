import streamlit as st
from PIL import Image

st.title('Section2：Python開発環境の構築')

st.text('PC上でPythonプログラムを作成・実行するためには、以下の準備を行う必要があります。')
st.markdown("""
1. Pythonのインストール
2. コードエディタのインストール
3. Python・コードエディタの連携
""")

st.text('それぞれの手順について、以下より解説していきます。')

st.header('1. Pythonのインストール')

st.text('1.1 以下のリンク(Python公式サイト)にアクセス')
st.markdown("[https://www.python.org/downloads/](https://www.python.org/downloads/)")

st.text('1.2 "Looking for a specific release?" 下のPython Version Listより"Python3.8.8"を探し、\nDownloadをクリック')
image = Image.open('Py-1.jpg')
st.image(image)

st.text('1.3 "Files"下のVersion ListよりWindows Installer(64-bit)を探し、クリック')
image = Image.open('Py-2.jpg')
st.image(image)

st.text('1.4 Installer(Python-3.8.8-amd64.exe)がダウンロードされるので、それをクリック')

st.text('1.5 管理者権限が要求されるため、IT部へ連絡・インストール手続きを進めてもらう')

st.text('※ここで、インストール時に以下の２点を実施してもらうよう、IT部の担当者に伝えてください。')

st.markdown("""
1. Add Python 3.8 to PATHにチェックを入れる
2. Install nowではなくCustomize Installationを選択し、すべてのチェックボックスにチェックを入れる
""")
image = Image.open('PY-3.jpg')
st.image(image)
st.text('これでPython自体のインストールは終了です。次に、PythonをPC上で動かすためのコードエディタをインストールします。')

st.header('2. コードエディタのインストール')
st.caption('ここでは、コードエディタの一つである「VSCode」のインストール・各種設定について解説します。')

st.text('2.1 以下のリンク(VSCode公式サイト)にアクセス')
st.markdown("[https://code.visualstudio.com/download](https://code.visualstudio.com/download)")

st.text('2.2 Windows用のDownloadリンクをクリック')
image = Image.open('VS-1.jpg')
st.image(image)

st.text('2.3 popの指示に従い、インストールを実行')

st.text('これでVSCodeのインストールは終了です。次に、VSCodeの拡張機能を用いて、Pythonと連携させます。')

st.header('Python・コードエディタの連携')
st.text('3.1 左端の「Extensions」アイコンをクリック')
image = Image.open('VS-2.jpg')
st.image(image)

st.text('3.2 検索バーに「Python」と入力')
image = Image.open('VS-3.jpg')
st.image(image)

st.text('3.3 表示されたPythonアイコン横の「インストール」をクリック')

st.text('3.4 インストール終了後、VSCodeを再起動')



st.text('※他にもVSCodeには様々な拡張機能が用意されています。\n快適な開発環境の構築のために、以下の拡張機能をインストールしておくことを\nお勧めします。')

st.subheader('・Japanese Language Pack for Visual Studio Code')
st.text(' メニュー・タブを日本語表示にする拡張機能')

st.subheader('・Python Indent')
st.text('for文などでインデントを行うと、Pythonの構文に従って自動的にインデントされる拡張機能')

st.subheader('・autoDocstring-Python Docstring Generator')
st.text('コード内に記載する説明文(Docstring)のフォーマットを自動生成する拡張機能')


st.text('以上でPythonの環境構築についての説明は終了です。\n次章では抑えておきたいPythonの基本的文法について解説します。')

