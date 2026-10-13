
import streamlit as st
import google.generativeai as genai

# --- ඔයා ලබාදුන් Gemini API Key එක මෙතනට ඇතුලත් කර ඇත ---
GOOGLE_API_KEY = "AQ.Ab8RN6LikQ5SkBQik_D-ciRlYpv_RBr5dk6QvvlgXTYcKy8FEg"

# Google AI Configure කිරීම
genai.configure(api_key=GOOGLE_API_KEY)

# පිටුවේ පෙනුම සකස් කිරීම
st.set_page_config(page_title="All-in-One AI Mega App", page_icon="🚀", layout="wide")
st.title("🚀 All-in-One AI Mega App")
st.write("ඔයාට අවශ්‍ය AI Tool එක වම්පස ඇති Menu එකෙන් තෝරාගන්න.")

# පැති මෙනුව (Sidebar Navigation)
menu = ["💬 AI Chatbot", "🎨 Image Generator", "🗣️ Voice Generator (TTS)", "🎬 Image to Video"]
choice = st.sidebar.selectbox("මෙනුව (Menu)", menu)

# =========================================================
# 1. AI CHATBOT SECTION
# =========================================================
if choice == "💬 AI Chatbot":
    st.header("💬 AI Chatbot")
    st.write("ඕනෑම ප්‍රශ්නයක් සිංහලෙන් හෝ ඉංග්‍රීසියෙන් අහන්න:")
    
    user_query = st.text_input("...ඔබේ ප්‍රශ්නය:")
    if st.button("පිළිතුර ලබාගන්න"):
        if user_query:
            with st.spinner("AI එක පිළිතුරු සපයමින් පවතී..."):
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(user_query)
                st.success("පිළිතුර:")
                st.write(response.text)
        else:
            st.warning("කරුණාකර ප්‍රශ්නයක් ඇතුළත් කරන්න.")

# =========================================================
# 2. IMAGE GENERATOR SECTION
# =========================================================
elif choice == "🎨 Image Generator":
    st.header("🎨 AI Image Generator")
    st.write("ඔයාට අවශ්‍ය පින්තූරය ඉංග්‍රීසියෙන් විස්තර කරන්න (Prompt):")
    
    image_prompt = st.text_area("Image Prompt (e.g., 'A futuristic city in Sri Lanka, realistic, 4k')")
    if st.button("පින්තූරය මවන්න"):
        if image_prompt:
            with st.spinner("AI එක පින්තූරය නිර්මාණය කරයි..."):
                imagen = genai.ImageGenerationModel("imagen-3.0-generate-002")
                result = imagen.generate_images(prompt=image_prompt, number_of_images=1)
                for image in result.images:
                    st.image(image._pil_image, caption="ඔබේ AI පින්තූරය")
        else:
            st.warning("කරුණාකර Prompt එකක් ඇතුළත් කරන්න.")

# =========================================================
# 3. VOICE GENERATOR SECTION
# =========================================================
elif choice == "🗣️ Voice Generator (TTS)":
    st.header("🗣️ AI Voice Generator")
    st.write("ඔබට හඬ බවට පත් කිරීමට අවශ්‍ය ලිපිය (Text) මෙතන ලියන්න:")
    
    text_to_speak = st.text_area("මෙහි ලියන්න:")
    if st.button("හඬ නිර්මාණය කරන්න"):
        if text_to_speak:
            with st.spinner("කටහඬ සකසමින් පවතී..."):
                tts_model = genai.GenerativeModel("gemini-2.0-flash")
                response = tts_model.generate_content([text_to_speak, "Convert this text into natural spoken audio speech."])
                st.success("හඬ සූදානම්!")
                st.audio(response.text) 
        else:
            st.warning("කරුණාකර ලිපියක් ඇතුළත් කරන්න.")

# =========================================================
# 4. IMAGE TO VIDEO SECTION
# =========================================================
elif choice == "🎬 Image to Video":
    st.header("🎬 AI Image to Video")
    st.write("ඔබේ ළඟ තියෙන පින්තූරයක් වීඩියෝවක් බවට පත් කරන්න මෙතනින් Upload කරන්න:")
    
    uploaded_file = st.file_uploader("පින්තූරයක් තෝරන්න...", type=["jpg", "png", "jpeg"])
    video_prompt = st.text_input("වීඩියෝ එකේ සිදුවිය යුතු චලනය විස්තර කරන්න (e.g., 'make the water move, cinematographic')")
    
    if st.button("වීඩියෝව සාදන්න"):
        if uploaded_file and video_prompt:
            with st.spinner("පින්තූරය වීඩියෝවක් බවට පත් කරමින් පවතී..."):
                video_model = genai.GenerativeModel("gemini-1.5-flash")
                from PIL import Image
                img = Image.open(uploaded_file)
                response = video_model.generate_content([img, f"Based on this image, describe the sequential video frames where: {video_prompt}"])
                st.info("වීඩියෝ සැලසුම සූදානම්:")
                st.write(response.text)
                st.caption("සටහන: නොමිලේ දෙන API මඟින් ඍජුවම Video File එකක් ලබාගැනීමට ඉදිරියේදී පහසුකම් තවත් යාවත්කාලීන වේ.")
        else:
            st.warning("කරුණාකර පින්තූරයක් සහ Prompt එකක් ලබා දෙන්න.")
