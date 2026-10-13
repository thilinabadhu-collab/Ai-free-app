import streamlit as st
import google.generativeai as genai
from PIL import Image

# --- ඔයාගේ Gemini API Key එක මෙතනට ඇතුලත් කරන්න ---
GOOGLE_API_KEY = AQ.Ab8RN6LikQ5SkBQik_D-ciRlYpv_RBr5dk6QvvlgXTYcKy8FEg

# Google AI Configure කිරීම
genai.configure(api_key=GOOGLE_API_KEY)

# පිටුවේ පෙනුම සකස් කිරීම
st.set_page_config(page_title="Thila AI Mega App", page_icon="🤖", layout="wide")
st.title("🤖 Thila AI Mega App")
st.write("ඔයාට අවශ්‍ය AI Tool එක වම්පස ඇති Menu එකෙන් තෝරාගන්න.")

# පැති මෙනුව (Sidebar Navigation)
menu = ["💬 AI Chatbot", "🖼️ Image Analyzer (පින්තූර විස්තර කිරීම)"]
choice = st.sidebar.selectbox("මෙනුව (Menu)", menu)

# =========================================================
# 1. AI CHATBOT SECTION
# =========================================================
if choice == "💬 AI Chatbot":
    st.header("💬 AI Chatbot")
    st.write("ඕනෑම ප්‍රශ්නයක් සිංහලෙන් හෝ ඉංග්‍රීසියෙන් අහන්න:")
    
    user_query = st.text_input("ඔබේ ප්‍රශ්නය මෙතන ලියන්න:")
    if st.button("පිළිතුර ලබාගන්න"):
        if user_query:
            with st.spinner("AI එක පිළිතුරු සපයමින් පවතී..."):
                model = genai.GenerativeModel('gemini-2.0-flash')
                response = model.generate_content(user_query)
                st.success("AI දුන් පිළිතුර:")
                st.write(response.text)
        else:
            st.warning("කරුණාකර ප්‍රශ්නයක් ඇතුළත් කරන්න.")

# =========================================================
# 2. IMAGE ANALYZER SECTION
# =========================================================
elif choice == "🖼️ Image Analyzer (පින්තූර විස්තර කිරීම)":
    st.header("🖼️ AI Image Analyzer")
    st.write("ඕනෑම පින්තූරයක් අප්ලෝඩ් කර එය ඇතුළේ තියෙන්නේ මොනවාදැයි AI එකෙන් අහන්න:")
    
    uploaded_file = st.file_uploader("පින්තූරයක් තෝරන්න...", type=["jpg", "png", "jpeg"])
    image_query = st.text_input("මේ පින්තූරය ගැන දැනගන්න ඕන දේ ලියන්න:", "Explain this image")
    
    if st.button("පින්තූරය පරීක්ෂා කරන්න"):
        if uploaded_file:
            with st.spinner("AI එක පින්තූරය කියවමින් පවතී..."):
                img = Image.open(uploaded_file)
                st.image(img, caption="ඔබ අප්ලෝඩ් කළ පින්තූරය", use_container_width=True)
                
                model = genai.GenerativeModel('gemini-2.0-flash')
                response = model.generate_content([image_query, img])
                st.success("AI විශ්ලේෂණය:")
                st.write(response.text)
        else:
            st.warning("කරුණාකර පින්තූරයක් අප්ලෝඩ් කරන්න.")
