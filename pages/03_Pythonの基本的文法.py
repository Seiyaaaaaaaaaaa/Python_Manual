import streamlit as st

st.title('Section3：Pythonの基本文法')
st.text('本ページでは抑えておきたいPythonの基本文法知識として、以下について解説します。')
st.markdown("""
1. 変数・データ型
2. 算術演算
3. for文
4. if文
5. def関数
6. class
""")

st.header('1. 変数・データ型')
st.text('Python上で値を入れる箱の役割を果たすものを「変数」と言います。\n変数に値を入れることを「代入」といい、代入後の変数は代入された値と等価であるとみなされ、\nPython上で処理されます。')
st.text('また変数に代入する値の種類のことを「データ型」といい、\nデフォルトでは以下のようなデータ型が用意されています。')
st.markdown("""
- 数値型
    - 整数型(int)
    - 浮動小数点型(float)
    - 複素数型(complex)
- シーケンス型
    - 文字列型(str)
    - リスト型(list)
    - タプル型(tuple)
- マッピング型
    - 辞書型(dict)
- 集合型
    - セット型(set)
    - フローズンセット型(frozenset)
- ブール型
    - ブール型(bool)
- NoneType
    - None
""")
st.text('※それぞれの具体的な内容は各種webサイトを参照のこと')

st.subheader('☕ データ型の設定について')
st.text('JAVAやC++では変数を実際に扱う前に「どの変数がどの型のデータを扱うか」を明示的に定義\n(型宣言)する必要があります。\n一方Pythonでは代入した値の型に合わせて変数の方も自動で変更されるという特徴があります。\nこの特性を「動的型付け」と呼び、Codeの短縮化に繋がっています。')

st.header('2. 算術演算')
st.text('Python上で算術演算を行うことができます。\n一般的な算術演算子は以下の通りです。')
st.subheader('加算：+')
code_ex = '''
a = 1
b = 3

C = a + b  #Calculation Result is 4
        
'''
st.code(code_ex, language='python')

st.subheader('減算：-')
code_ex = '''
a = 8
b = 5

C = a - b  #Calculation Result is 3
        
'''
st.code(code_ex, language='python')

st.subheader('乗算：*')
code_ex = '''
a = 3
b = 6

C = a * b  #Calculation Result is 18
        
'''
st.code(code_ex, language='python')

st.subheader('除算：/')
code_ex = '''
a = 5
b = 3

C = a /  b  #Calculation Result is 1.6666666666666667
C = a // b  #Calculation Result is 1 (integer division)
        
'''
st.code(code_ex, language='python')

st.subheader('剰算：%')
code_ex = '''
a = 5
b = 3

C = a % b  #Calculation Result is 2
        
'''
st.code(code_ex, language='python')

st.subheader('冪乗：**')
code_ex = '''
a = 2
b = 3

C = a ** b  #Calculation Result is 8
        
'''
st.code(code_ex, language='python')

st.text('また、データ型がstr(文字列型)であっても、足し算のみは行うことができます。')
code_ex = '''
a = 'Hello,'
b = 'MODEC!'

C = a + b  #Calculation Result is 'Hello,MODEC!'
        
'''
st.code(code_ex, language='python')


st.header('3. for文')

st.text('「Pythonの基礎知識」のページにて、Computer Programは指定した動作の反復が得意であることを\n説明しました。\nその反復動作を実行させるPythonの命令を「for文」といいます。')
st.text('for文の使用方法として、2つのケースのコード例を下に示します。')
st.subheader('1. 反復回数を直接指定するケース')

code_ex = '''
a = 0

for i in range(10): #Repeat INDENTED calculation 10 times

    a += 1  #The same meaning as "a = a + 1"
    print('a = ' + str(a))
    
-----------------------------------------
a = 1
a = 2
  .
  .
  .
a = 10
        
'''
st.code(code_ex, language='python')

st.subheader('2. listの要素数だけ反復動作を行うケース')
code_ex = '''
product = 1
numbers = [2,3,4,5] #difinition of list

for number in numbers: #Assign each element of list "numbers" to "number"

    product *= number  #The same meaning as "product = product * number"
    print('product = ' + str(product))
    
-----------------------------------------
product = 2
product = 6
product = 24
product = 120
        
'''
st.code(code_ex, language='python')


st.header('4. if文')
st.text('Pythonではif文を使うことによって、操作の条件分岐を行うことができます。')

code_ex = '''
sum = 0
equation = str(sum)

numbers = [2, 3, 4, 5, 6, 7, 8] #difinition of list"numbers"

for number in numbers: #Assign each element of list "numbers" to "number"
    if number > 5: #If the number is larger than 5, execute following INDENDED calculation
        sum += number
        equation = equation + '+' +  str(number)
        st.write('sum = ' + str(sum) + ' (' + equation + ') ')

-----------------------------------------
sum = 6 (0+6)
sum = 13 (0+6+7)
sum = 21 (0+6+7+8)
        
'''
st.code(code_ex, language='python')

st.header('5. def関数')
st.text('同じ計算処理を離れた箇所で複数回行いたいとき、\nその計算操作をdef関数として定義しておくと、同一のコーディングを複数回行う必要がなくなります。')
st.text('def関数は以下のように構成されます。')
code_ex = '''
def "Function Name"("Parameter Variable1", "Parameter Valiable2", ...):
    "Function Body"
          .
          .
          .
    return "Return Value"

'''
st.code(code_ex, language='python')

st.text('サンプルコードは以下の通りです。')
code_ex = '''
def STEM_ave(scores):
    math_score = scores.get('math')
    science_score = scores.get('science')

    average = (math_score + science_score) / 2

    return average
    
    
scores_Tom = {'math': 85, 'science': 90, 'literature': 51, 'politics' = 84}
scores_Joe = {'math': 68, 'science': 87, 'literature': 88, 'politics' = 69}

average_Tom = STEM_ave(scores_Tom) 
average_Joe = STEM_ave(scores_Joe) 

print('Toms STEM Average Score is' + ' ' +  str(average_Tom))
print('Joes STEM Average Score is' + ' ' +  str(average_Joe))

-----------------------------------------
Toms STEM Average Score is 87.5
Joes STEM Average Score is 77.5

'''
st.code(code_ex, language='python')

st.header('6. class')
st.text('大規模programになると、def関数の数・引数に用いる変数の数も膨大になります。\n複数のdef関数・引数データをひとまとめにして、管理しやすくしたものをclassといいます。')
st.text('classの基本構造は以下の通りです。')
code_ex = '''
class "Class Name":
    def __init__(self): #Constructor to initialize instance valiables
        "Initializer Body"
                .
                .
                .
    def "Function(Method) Name"("self, Parameter Variable1", "Parameter Valiable2", ...):
        "Function Body"
              .
              .
              .
          

'''
st.code(code_ex, language='python')

st.text('サンプルコードは以下の通りです。')
code_ex = '''
class average_calculation:
    def __init__(self, scores): 
        self.math = scores["math"]
        self.science = scores["science"]
        self.literature = scores["literature"]
        self.politics = scores["politics"]
        
    def STEM_ave(self):
        average = (self.math + self.science) / 2

        return average
        
    def LibArts_ave(self):
        average = (self.literature + self.politics) / 2

        return average

scores_Tom = {'math': 85, 'science': 90, 'literature': 51, 'politics': 84}
scores_Joe = {'math': 68, 'science': 87, 'literature': 88, 'politics': 69}

Tom_score_report = average_calculation(scores_Tom)
Joe_score_report = average_calculation(scores_Joe)

average_STEM_Tom = Tom_score_report.STEM_ave()
average_STEM_Joe = Joe_score_report.STEM_ave()
average_LibArts_Tom = Tom_score_report.LibArts_ave()
average_LibArts_Joe = Joe_score_report.LibArts_ave()

print('Toms STEM Average Score is' + ' ' +  str(average_STEM_Tom))
print('Joes STEM Average Score is' + ' ' +  str(average_STEM_Joe))
print('Toms LibArts Average Score is' + ' ' +  str(average_LibArts_Tom))
print('Joes LibArts Average Score is' + ' ' +  str(average_LibArts_Joe))

-----------------------------------------
Toms STEM Average Score is 87.5
Joes STEM Average Score is 77.5
Toms LibArts Average Score is 67.5
Joes LibArts Average Score is 78.5
'''
st.code(code_ex, language='python')


st.text('これで押さえておきたいPythonの基本文法の解説は終了です。\n次章では、データ分析に特化したライブラリである「pandas」について解説します。')