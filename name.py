import streamlit as st

st.title('나의 첫 웹 서비스 제작')
name = st.text_input('당신의 이름은?')
menu = st.selectbox('가장 많이 사용하는 SNS는?', ['인스타', '카카오톡', '유튜브'])
time = st.slider('하루 사용 시간은?', 0, 12, 3) 

if st.button('나의 디지털 습관'): 
    st.write(f'{name}님은 {menu}를 {time}동안 사용합니다.')
    st.balloons()
