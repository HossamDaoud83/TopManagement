import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="GSB", page_icon="16.png")
st.image("GSB Medium.png", width=120,)
st.title("GSB Results System")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.text("Laila AI Virtual Assistant Overview")
st.video("https://youtu.be/ZBbsxCnzz5Y?si=BHxPwJh5V-FuT5Qi")

st.text("Graduate School of Business Overview")
st.video("https://youtu.be/Jrmxt2gDTYk?si=lg72Qa2BNf5Z2rq_")

st.text("Business Development Center - BDC Overview")
st.video("https://youtu.be/AcWcvEh7ZKo?si=3T7JSLRIQSDjhbtw")

st.text("Master of Business Administration - Majors")
st.video("https://youtu.be/QUByDhfAtp0")

st.text("التخصصات في ماجستير إدارة الأعمال")
st.video("https://youtu.be/8MTm74uZKxk")
