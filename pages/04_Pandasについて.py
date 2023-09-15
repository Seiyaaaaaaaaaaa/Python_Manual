import streamlit as st
import pandas as pd
from PIL import Image

st.title('Section4：pandasについて')
st.caption('ここでは数多くあるPyhton用ライブラリのうち、pandasについてその概要・活用方法を説明します。')
st.header('1. pandasとは')
st.text('データ分析に特化したPython用外部ライブラリ。\n表形式のデータを「dataframe」という型の変数で扱うことで、\nExcelのような体感的操作が可能であることが特徴です。')
st.text('Engineering業務ではExcelベースの表形式データを扱うことが多くあるため、\npandasはPython×Engineeringで強力なツールとなり得るでしょう。')

st.header('2. dataframeとは')
st.text('dataframeとはpandas上で扱う表形式のデータで、基本構成は以下の通りです。')

image = Image.open('pd-1.jpg')
st.image(image)

st.header('3. pandasでできること')
st.text('pandasを用いて行うことができるデータ処理のうち、代表的なものについて以下の順に説明します。')
st.markdown("""
1. Excelからデータを読み込む
2. 特定のデータの抽出
3. 列単位での演算・加工
4. map + lambda式
""")

st.subheader('1. Excelからデータを読み込む')
st.text('pandasでは"read_excel"メソッドを使うことで、\n特定のExcelファイルからdataframeの形でデータを取得することが可能です。')
st.text('例えば以下のデータを持つExcel File "Score_Sheet.xlsx"があったとき、')
image = Image.open('pd-2.jpg')
st.image(image)
st.text('"read_excel"メソッドを呼び出すことで、Excel上のデータをdataframeの形で取得できます。')
code_ex = '''
import pandas as pd 

df = pd.read_excel('Score_Sheet.xlsx')

'''
st.code(code_ex, language='python')

df = pd.read_excel('Score_Sheet.xlsx')

st.text('出力結果')
st.write(df)

st.text('また以下のようにindexに用いるColumnを指定することで、\nrawの値を表内のデータに設定することもできます。')
code_ex = '''
import pandas as pd 

df = pd.read_excel('Score_Sheet.xlsx', index_col='NAME') #Set "NAME" column as raw

'''
st.code(code_ex, language='python')

df = pd.read_excel('Score_Sheet.xlsx', index_col='NAME') 

st.text('出力結果')
st.write(df)

st.subheader('2. 特定のデータの抽出')
st.text('pandasではdataframeに格納されているデータの中から、\n特定の条件を満たすデータのみを抽出することができます。')
code_ex = '''
import pandas as pd 

df = pd.read_excel('Score_Sheet.xlsx', index_col='NAME') #Set "NAME" column as raw

df_Young_GoodScore = df[(df['AGE']<16)&(df['SCORE']>70)]
    #extract data which "AGE is less than 16" & "SCORE is larger than 70"


'''
st.code(code_ex, language='python')

df = pd.read_excel('Score_Sheet.xlsx', index_col='NAME') #Set "NAME" column as raw

df_Young_GoodScore = df[(df['AGE']<16)&(df['SCORE']>70)]
    
st.text('出力結果')
st.write(df_Young_GoodScore)

st.subheader('3. 列単位での演算・加工')
st.text('pandasではdataframeの列単位での一斉演算が可能です。')
code_ex = '''
import pandas as pd 

df = pd.read_excel('Score_Sheet.xlsx', index_col='NAME') #Set "NAME" column as raw

df['SCORE'] += 5 #Add 5 to All Scores
    
'''

st.code(code_ex, language='python')

df = pd.read_excel('Score_Sheet.xlsx', index_col='NAME') #Set "NAME" column as raw

df['SCORE'] += 5
    
st.text('出力結果')
st.write(df)

st.text('また"loc"メソッドと組み合わせることで、特定の条件を満たす行のみに演算処理を行うことも可能です。')

code_ex = '''
import pandas as pd 

df = pd.read_excel('Score_Sheet.xlsx', index_col='NAME') #Set "NAME" column as raw

df.loc[df['AGE'] <16, 'SCORE'] += 5
    #Add 5 to Scores for Members under 16 years old
'''

st.code(code_ex, language='python')

df = pd.read_excel('Score_Sheet.xlsx', index_col='NAME') #Set "NAME" column as raw

df.loc[df['AGE'] <16, 'SCORE'] += 5
    #Add 5 to Scores for Members under 16 years old

st.text('出力結果')
st.write(df)

st.subheader('4. map + lambda式')
st.text('mapとlambda式を組み合わせることで、dataframeに対するより複雑な演算処理を行うことができます')

code_ex = '''
import pandas as pd 

df = pd.read_excel('Score_Sheet.xlsx', index_col='NAME') #Set "NAME" column as raw

df['Result'] = df['SCORE'].map(lambda x: 'Pass' if x >= 60 else 'Fail')
    #Add New Column named "Result" that displays;
    #    "Pass" : SCORE >= 60 
    #    "Fail" : SCORE <  60 
'''

st.code(code_ex, language='python')

df = pd.read_excel('Score_Sheet.xlsx', index_col='NAME') #Set "NAME" column as raw

df['Result'] = df['SCORE'].map(lambda x: 'Pass' if x >= 60 else 'Fail')
st.text('出力結果')
st.write(df)

st.text('以上がpandasに関する基礎的な解説でした。より詳しい解説は各種webサイト等を参照ください。')
st.text('次章ではPythonの強みの一つである「他ソフトウェアとの連携」について解説します。')




