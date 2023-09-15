import streamlit as st
import pandas as pd


st.title('Section1：Pythonの基礎知識')
st.caption('Pythonとは何か・どういったことができるのかについて簡単にまとめています')
st.header('1. Pythonとは？')
st.text('インタプリタ型に分類されるプログラミング言語。\nそのシンプルさ＆高機能さゆえに、数多くのシステム・webアプリケーションに利用されています。')
st.header('2. Pythonの特徴')
st.text('ここからはPythonの特徴を紹介しつつ、なぜEngineering領域でPythonが強力なツールと\nなりえるのかについて解説します。')
st.text('他言語と比較してPythonが持つ特徴は下記が挙げられます')
st.subheader('・文法が平易')
st.text('同じようなFunctionを持つコードを作成したいとき、\nPythonを用いるとJAVA・C++等の多言語と比較して、コード長が短くなる傾向にあります。')
#st.text('例) のコード例')

#st.text('--------------JAVA・`Pythonのコード比較例を載せる予定--------------')

code_py = '''
コード例書くよ！！！！！！！！！！！！！！！！！！
        
'''

code_c = '''
コード例書くよ！！！！！！！！！！！！！！！！！！
        
'''

#st.code(code_py, language='python')
#st.code(code_c, language='C++')

st.text('これはPythonはインタプリタ型言語であるため、JAVA・C++で必要とされる「型宣言」\n(変数データの種類を明示的に定義する操作)が不要であることが理由です。')

st.subheader('・ライブラリが豊富')
st.text('Pythonには複数のライブラリ(特定の機能を備えているパッケージ)が用意されています。\nこれによって、複雑なコーディングを行うことなく、高度な演算処理を行うことが可能となります。')
st.text('※代表的なライブラリ例')

df = pd.read_excel('Library_example.xlsx', index_col='LIBRARY NAME')
st.dataframe(df)



st.header('3. Python×Engineering')
st.caption('最後に、EngineeringにPython導入することによるメリットについて説明します。')

st.subheader('・Routine Workの自動化')
st.text('Computer Programの特徴として、あらかじめ指定した動作の「反復」が得意であることが挙げられます。\nEngineering業務の中にはRoutine Workも数多くあるため、\nPythonに適切な指示を出すだけで大幅な業務量削減が見込めます。')

st.subheader('・ソフトウェア間連携による業務の自動化・最適化')
st.text('Engineering業務では複数のソフトウェアを使用することが多く、\nソフトウェア操作の習得度によって作業時間・アウトプットに相当の差が生じえます。')
st.text('上述の「ライブラリ」の中には、他ソフトウェアとの連携に特化したものが数多くあるため、\n各ソフトウェアのデータ連携・操作をPythonによって一元的に管理することができれば、\n業務効率の大幅な向上が期待されます。')
st.text('※本機能についてはSection6にて詳しく解説していますので、そちらをご参照ください。')
st.text('以上がPythonに関する基礎的な説明でした。\n次章ではPythonを使うための前準備として、「Python開発環境の構築」について解説します。')
