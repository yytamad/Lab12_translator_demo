import streamlit as st 
# https://pypi.org/project/googletrans-py/ 
# pip install googletrans-py
from googletrans import Translator
import time

st.set_page_config(page_title="Language Translation", page_icon="🌐")

@st.cache_resource(show_spinner="Initializing...")
def get_translator():
  return Translator()

translator = get_translator()

def do_translation():
    with st.empty():
      with st.status("Translating ...") as status:
        out = translator.translate(st.session_state.src, dest=st.session_state.lang)
        status.update(label="Done!", state="complete")
        time.sleep(0.5)
      with st.expander("**View translation**"):
        st.write(out.text)
 
st.markdown("## :rainbow[Machine Translation]")

default_text = """Artificial intelligence (AI) has been used in applications throughout industry and academia. Similar to electricity or computers, AI serves as a general-purpose technology that has numerous applications. 
Its applications span language translation, image recognition, decision-making, credit scoring, e-commerce and various other domains.
"""
with st.form("translate"):
   # https://developers.google.com/admin-sdk/directory/v1/languages
    source_text = st.text_area("Enter text to translate:", default_text, height=200, key="src")
    target_language = st.selectbox("Select target language:", 
                                   ["Chinese (Traditional)", "Chinese (Simplified)", "French", "German", "Hindi", "Indonesian", "Japanese", "Korean"], 
                                   key="lang")
    translate = st.form_submit_button('Translate')

if translate:
    do_translation()