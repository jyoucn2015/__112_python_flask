import streamlit as st

genre = st.radio(
    "您喜歡的節目是什麼",
    ('動畫', '戲劇', '記錄片'))

if genre == '動畫':
    st.write('你選擇動畫')
elif genre == '戲劇':
    st.write('你選擇戲劇')
elif genre == '記錄片':
    st.write('你選擇記錄片')