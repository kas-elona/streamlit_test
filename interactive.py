from PIL import Image

import streamlit as st
import time

st.title('Streamlit インタラクティブ編')

# プログレスバー
overwrite = st.empty()
overwrite.text('START')

latest_itelation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_itelation.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.05)
overwrite.text('DONE')

# カラムレイアウト変更
left_column, right_column = st.columns(2)
with left_column:
    button = st.button('Display text in the right column.')
with right_column:
    if button:
        st.write('This is the right column.')

# エクスパンダー
expander = st.expander('What is the purpose of this site?')
expander.write('This site is for practicing interactive widgets.')

# チェックボックス
if st.checkbox('Show Image'):
    img = Image.open('yurayuraNYN.gif')
    st.image(img,
             caption='ゆらゆらNYN姉貴',
             use_column_width = 'auto',
             )

# セレクトボックス
option_select = st.selectbox(
    'What is your favorite number?',
    list(range(1, 11)),
)
'Your favorite number is ', option_select, '.'

# テキストボックス
option_text = st.text_input(
    'What are your hobbies?'
)
'Your favorite hobbies is ', option_text, '.'

# スライダー
condition = st.slider('How are you doing now?', min_value=0, max_value=100, value=30, step=5)
'Your condition: ', condition

# ラジオボタン（サイドバー）
st.sidebar.radio(
    'What is your GENDER?',
    ['F', 'M', 'A'],
    horizontal = True 
)


