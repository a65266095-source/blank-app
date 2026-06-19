import streamlit as st
import yt_dlp
import os

# App Ki Styling
st.set_page_config(page_title="Amit YT Downloader", page_icon="🎥", layout="centered")
st.title("🎥 Amit Ka YouTube Video Downloader")
st.write("Kal se chal rahi mehnat ka result! Link dalo aur video download karo.")

# Input Box
video_url = st.text_input("Yahan YouTube Video Ka Link Paste Karo 👇")

if st.button("Video Download Karo 🚀"):
    if video_url:
        try:
            st.info("Video fetch ho rahi hai, thoda sabr rakho bhai...")
            
            # Simple Download Options
            ydl_opts = {
                'format': 'best',
                'outtmpl': '%(title)s.%(ext)s',
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(video_url, download=True)
                filename = ydl.prepare_filename(info)
                
            st.success(f"🎉 Kamiyabi! Video download ho gayi hai: {filename}")
            
            # Mobile me save karne ke liye Download Button
            with open(filename, "rb") as file:
                st.download_button(
                    label="📱 Apne Phone Me Save Karo",
                    data=file,
                    file_name=filename,
                    mime="video/mp4"
                )
        except Exception as error:
            st.error(f"Arre yaar, koi dikkat aayi: {error}")
    else:
        st.warning("Pehle link toh dalo bhai!")
        
