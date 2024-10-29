'''
streamlit多页面程序的入口文件
'''
from tkinter import Image

import streamlit as st
st.title("AI大模型应用产品网")
col,col1,col2 = st.columns(2)

with col:
    st.image(Image.open('img1.jpg'))
    st.button("jory慧言")
    st.switch_page("pages/demo.py")


# c1,c2,c3 = st.columns(3)
# with c1:
#     flag = st.button("基础版")
#     if flag:
#         st.switch_page("pages/demo.py")
# with c2:
#     flag1 = st.button("进阶版")
#     if flag1:
#         st.switch_page("pages/demo-history.py")
# with c3:
#     flag2 = st.button("文生图")
#     if flag2:
#         st.switch_page("pages/textTOImage.py")
