import streamlit as st
from PIL import Image


st.title('Section7：生成AIの活用')
st.text('これまでの記事を通して、Pythonの基本知識について解説してきました。\n以前までであればこれらの知識を用いて自らの手でCoding→Bug対処という流れで開発が行われてきましたが、\nChatGPTをはじめとした生成AIの出現・高度化により、ユーザー自身がコーディングを行う必要性は大幅に減少しました。')
st.text('本ページでは生成AIを用いたPythonのCoding・および活用時の注意点について解説します。')

st.header('1. 生成AIとは')
st.text('生成AIとは、ユーザーからのコマンドに応答してテキスト・画像・その他メディアを\n生成することができる人工知能の一種です。\n代表的なものとしては、OpenAI社の"ChatGPT"、Microsoft社の"Bing Chat"等がありますが、\n本ページではBing Chatを用いて解説を進めていきます。')
st.header('2. Coding活用例')
st.text('例えば、「dataframe内の特定の条件を満たす行を検索し、その行の特定列の要素を表示するpythonのコード」を書きたい場合、\n生成AI普及以前であれば、pandasに関する書籍・web記事を参照しなければ難しかったでしょう。')
st.text('しかし現在は、AI Chatにそのまま要求を書き込むだけで、\n自動的に正しいCodeを作成させることが可能です。')
image = Image.open('AI-1.jpg')
st.image(image)

st.text('したがって、今後Engineerに求められるPythonスキルはCodingに関する知識・経験ではなく、\nAI Chatに正しく指令を投げること、つまり前述の「ロジックツリー」を正しく理解し・作成すること\nであると言えるでしょう。')

st.header('3. 生成AIを用いるうえでの注意点')
st.text('一見万能ツールに思える生成AIですが、情報セキュリティの観点からまだ万全とは言えず、\nMODEC社内でもChatGPTの使用は禁止されています(2023年9月現在)。\nこの状況を受けてMOPSのDnAチームでは、社内利用を意図した高度生成AIである\n「MODEC AI」の開発が進んでいます。\nその機能・活用方法については、MODEC AIリリース後、本ページで紹介したいと思います。')
