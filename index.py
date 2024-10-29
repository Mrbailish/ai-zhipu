import streamlit as st
st.title("🙋🙋 AI大模型应用产品网 🙋🙋")
col,col1, = st.columns(2)

with col:
    st.image("https://imgs.699pic.com/images/601/338/156.jpg!list2x.v1",use_column_width=True)
    flag = st.button("绘声绘色",use_container_width=True)
    if flag:
        st.switch_page("pages/demo-history.py")
#
with col1:
    st.image("https://imgs.699pic.com/images/400/913/760.jpg!list2x.v1", use_column_width=True)
    flag = st.button("绘图绘画",use_container_width=True)
    if flag:
        st.switch_page("pages/textToImage.py")
