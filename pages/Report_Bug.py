import warnings

import requests
import streamlit as st
from streamlit_lottie import st_lottie

warnings.filterwarnings("ignore")
st.set_page_config(page_title='NextReach', page_icon="📝", layout="wide")

# hide menu

hide_menu = """
<style>
#MainMenu{
visibility:hidden;
}
footer{visibility:hidden;}
 footer:after{
   visibility:visible;
   content:'Copyright @ 2023: Nabil Nabawi';
   display:block;
   position:relative;
   color:white;
 }
</style>
"""

# open css file
with open('style2.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(\
                    https://raw.githubusercontent.com/nabilnabawi1234/projectpython/main/logo320.png\
                );
                background-repeat: no-repeat;
                padding-top: 150px;
                background-position: 5px 5px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "        ";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


add_logo()
st.markdown(hide_menu, unsafe_allow_html=True)

original_title1 = '<p style="font-family:Arial;text-align:center; color:white; font-size: 50px;">\
    <strong>REPORT BUG</strong>\
        </p>'
st.write(original_title1, unsafe_allow_html=True)


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style2.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/99073c09-49f0-468a-bb77-0355534e82b1/qtnfyqnBId.json")
# img_contact_form = Image.open("images/yt_contact_form.png")
# img_lottie_animation = Image.open("images/yt_lottie_animation.png")


# ---- CONTACT ----
with st.container():
    st.write("---")
    st.write("##")

contact_form = """
    <form action="https://formsubmit.co/ziyan.offl@gmail.com" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Your name" required>
                <input type="email" name="email" placeholder="Your email" required>
                <textarea name="message" placeholder="Your message here" required></textarea>
                <button type="submit">Send</button>
    </form>
                """
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    # st.empty()
    st_lottie(lottie_coding, height=300, key="coding")
