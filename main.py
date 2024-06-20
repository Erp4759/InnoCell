import streamlit as st
from multiapp import MultiApp
from apps import Home, About, Login, Upload

# Hide Streamlit warnings using HTML and CSS
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .css-1vbd788 {visibility: hidden;}
            .stException {display: none;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

app = MultiApp()

# Добавьте все ваши приложения сюда
app.add_app("Home", Home.app)
app.add_app("About", About.app)
app.add_app("Login", Login.app)
app.add_app("Upload", Upload.app)

# Проверьте статус логина
Login.check_login_status()

app.run()
