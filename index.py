import streamlit as st
st.title("🙋🙋 AI大模型应用产品网 🙋🙋")
col,col1, = st.columns(2)

with col:
    st.image("https://t7.baidu.com/it/u=2656780661,2835874604&fm=193&f=GIF",use_column_width=True)
    flag = st.button("绘言",use_container_width=True)
    if flag:
        st.switch_page("pages/demo-history.py")
#
with col1:
    st.image("https://t7.baidu.com/it/u=2656780661,2835874604&fm=193&f=GIF", use_column_width=True)
    flag = st.button("绘图",use_container_width=True)
    if flag:
        st.switch_page("pages/textToImage.py")
