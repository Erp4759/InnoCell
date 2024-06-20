import streamlit as st
from PIL import Image

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
    st.title("Upload Image")
    if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
        st.error("You must be logged in to upload images")
        return

    uploaded_file = st.file_uploader("Choose an X-ray image...", type="jpg")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("")
        st.write("Classifying...")
        # Имитация отправки изображения для классификации
        # В реальном случае здесь будет вызов модели
        st.success("Image classified successfully!")
