import streamlit as st

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
        st.success(f"Metin: {text_to_translate}")
        st.success(f"Seçilen Dil: {languages[target_language]}")
    else:
        st.warning("Lütfen metin girin ve bir dil seçin.")


