import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="GSB", page_icon="16.png")
st.image("GSB Medium.png", width=120,)

st.title("GSB Results System")
components.iframe("https://app.powerbi.com/view?r=eyJrIjoiZjc0NDRiNDctMTQ1Yy00ZGRhLWEzYzgtZDIzM2ViYTY0ZDQ2IiwidCI6ImE0NzRkYzY0LTQ1ZDEtNDNkOS05N2FjLWM4NWY0ZDMyZmUwMCIsImMiOjl9&embedImagePlaceholder=true", width=800, height=600)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
