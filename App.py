import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="GSB", page_icon="16.png")

def main():
    st.image("GSB Medium.png", width=120,)
    st.title("Graduate School of Business 🏫")
    st.title("GSB Payment System")
    components.iframe("https://app.powerbi.com/view?r=eyJrIjoiNzhmYzA2YzktMWJmOC00MGM2LWJmMWEtM2I3ZjhjZDk1MDgyIiwidCI6ImE0NzRkYzY0LTQ1ZDEtNDNkOS05N2FjLWM4NWY0ZDMyZmUwMCIsImMiOjl9", width=600, height=600)
    
    st.title("GSB USD Analysis System")
    components.iframe("https://app.powerbi.com/view?r=eyJrIjoiMWI3YWM1MjUtYjU0Yi00NzVkLWFmNDctNWMxNzVhMTUwZjZhIiwidCI6ImE0NzRkYzY0LTQ1ZDEtNDNkOS05N2FjLWM4NWY0ZDMyZmUwMCIsImMiOjl9", width=600, height=600)
    
    st.title("GSB Evaluation System")
    components.iframe("https://app.powerbi.com/view?r=eyJrIjoiNTgzMjVlNzUtYmI2NC00NjhkLWJhMjItYzJmZThlOWUzMzQzIiwidCI6ImE0NzRkYzY0LTQ1ZDEtNDNkOS05N2FjLWM4NWY0ZDMyZmUwMCIsImMiOjl9", width=600, height=600)
    
    st.title("GSB Results System")
    components.iframe("https://app.powerbi.com/view?r=eyJrIjoiZjc0NDRiNDctMTQ1Yy00ZGRhLWEzYzgtZDIzM2ViYTY0ZDQ2IiwidCI6ImE0NzRkYzY0LTQ1ZDEtNDNkOS05N2FjLWM4NWY0ZDMyZmUwMCIsImMiOjl9&embedImagePlaceholder=true", width=600, height=600)


if __name__ == "__main__":
    main()
