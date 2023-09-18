import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="GSB", page_icon="16.png")

st.image("GSB Medium.png", width=120,)
st.title("Graduate School of Business 🏫")
st.image("Power-Bi-Service.jpg", width=600,)


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
