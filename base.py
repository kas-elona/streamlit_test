from PIL import Image

import streamlit as st
import numpy as np
import pandas as pd
import base64

st.title('Streamlit 超入門')

### 表 ###
st.write('# DataFrame')

# ソース
df_graph = pd.DataFrame({
    'Col1': [1, 2, 3, 4],
    'Col2': [10, 20, 30, 40]
})

# 表の追加
st.write(df_graph)
st.dataframe(df_graph.style.highlight_max(axis=0), width=680, height=175) # DYNAMICな表
st.table(df_graph) # STATICな表


### MAZIC COMMAND = MARK DOWN ###
"""
# 章
## 節
### 項

### import list
```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

### チャート ###
# ソース
df_chart = pd.DataFrame(
    np.random.rand(20, 3),
    columns = ['Col1', 'Col2', 'Col3']
)

# 折れ線
st.write('### 折れ線')
st.line_chart(df_chart)

# エリア
st.write('### エリア')
st.area_chart(df_chart)

# バー
st.write('### バー')
st.bar_chart(df_chart)

### マップ ###
# ソース
df_map = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns = ['lat', 'lon']
)

# マップ
st.write('### マップ')
st.map(df_map)

### 画像 ###
st.write('Display Image')

# 読み込み
img = Image.open('yurayuraNYN.gif')

# 表示
st.write('### 画像')
st.image(img, caption='ゆらゆらNYN姉貴', use_column_width=True)

# GIFとして読み込む
file_ = open('.\yurayuraNYN.gif', 'rb')
contents = file_.read()
data_url = base64.b64encode(contents).decode('utf-8')
file_.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="ゆらゆらNYN姉貴">',
    unsafe_allow_html=True,
)
