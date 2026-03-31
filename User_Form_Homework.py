import streamlit as st

submitted_agree = 0
with st.form('my_form'):
    st.subheader("사용자 입력 폼")
    name = st.text_input('이름')
    age = st.number_input('나이', min_value=0, step=1)
    term_checkbox = st.checkbox('약관에 동의합니다.')
    submitted = st.form_submit_button('제출')
    if(term_checkbox and submitted and name and age):
        submitted_agree = 1
if submitted_agree:
    st.write(f"이름 : {name}, 나이 : {age}")
    st.success('약관에 동의했습니다.')