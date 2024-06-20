import streamlit as st
from userdata.database import add_user, authenticate_user

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

def app():
    st.title("Login")

    menu = ["Login", "Sign Up"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Login":
        st.subheader("Login Section")

        username = st.text_input("Username")
        password = st.text_input("Password", type='password')
        if st.button("Login"):
            if authenticate_user(username, password):
                st.success("Logged In as {}".format(username))
                st.experimental_set_query_params(logged_in="true", username=username)
                st.session_state['logged_in'] = True
                st.session_state['username'] = username
            else:
                st.error("Invalid username or password")

    elif choice == "Sign Up":
        st.subheader("Create New Account")

        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type='password')
        if st.button("Sign Up"):
            if add_user(new_username, new_password):
                st.success("Account created successfully")
                st.info("Go to Login Menu to login")
            else:
                st.warning("Username already exists")

def check_login_status():
    params = st.experimental_get_query_params()
    if 'logged_in' in params and 'username' in params:
        st.session_state['logged_in'] = True
        st.session_state['username'] = params['username'][0]
    else:
        st.session_state['logged_in'] = False
