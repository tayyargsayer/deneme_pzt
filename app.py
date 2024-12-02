import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
# Configure the generative AI model
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 81920,
    "response_mime_type": "text/plain",
}


model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Function to translate text
def translate_text(text, target_language):
    response = model.generate_content(f"Translate the following text to {target_language}: {text}")
    return response.text

st.title("Metin Girişi ve Dil Seçimi")

# Kullanıcıdan metin girişi
text_to_translate = st.text_area("Çevrilecek metni girin:")

# Hedef dili seçin
languages = {
    'İngilizce': 'en',
    'İspanyolca': 'es',
    'Fransızca': 'fr',
    'Almanca': 'de',
    'Çince': 'zh',
    'Japonca': 'ja',
    'Korece': 'ko'
}

target_language = st.selectbox("Hedef dili seçin:", list(languages.keys()))

if st.button("Gönder"):
    if text_to_translate and target_language:
        translated_text = translate_text(text_to_translate, languages[target_language])
        st.success(f"Çevrilen Metin: {translated_text}")
    else:
        st.warning("Lütfen metin girin ve bir dil seçin.")


