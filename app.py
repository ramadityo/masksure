import streamlit as st
from PIL import Image
from detection import Detection
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(page_title="Object Detection Web App - Viskom")

st.write(
    """
    # Object Detection Web App

    Selamat datang di Aplikasi Object Detection sederhana! 🚀 Aplikasi ini dikhususkan untuk memenuhi
    syarat Ujian Akhir Semester dari Visi Komputer. Aplikasi ini dibuat untuk mendeteksi orang
    yang memakai masker maupun tidak. Selamat mencoba!
    """
)

# st.image("assets/20241128_214330_masksure.png")

UPLOAD_IMAGE = st.file_uploader("Choose a file")

if UPLOAD_IMAGE is not None:
    img = Image.open(UPLOAD_IMAGE)
    img = img.resize((img.width // 2, img.height // 2))
    st.image(img)

    if st.button("Deteksi gambar!"):
        img_result, stats = Detection.detect(img)
        st.image(img_result)

        st.write("## Statistik 📈")

        PREPROCESS_MILISEC = float(stats['preprocess']) * 1000
        PREPROCESS_MILISEC = round(PREPROCESS_MILISEC / 1000, 1)

        INFERENCE_MILISEC = float(stats['inference']) * 1000
        INFERENCE_MILISEC = round(INFERENCE_MILISEC / 1000, 1)

        POSTPROCESS_MILISEC = float(stats['postprocess']) * 1000
        POSTPROCESS_MILISEC = round(POSTPROCESS_MILISEC / 1000, 1) 

        data = {
            'Stage': ['Preprocess', 'Inference', 'Postprocess'],
            'Time (ms)': [PREPROCESS_MILISEC, INFERENCE_MILISEC, POSTPROCESS_MILISEC]
        }

        df = pd.DataFrame(data)
        st.table(df)
        df = df.set_index('Stage')

        st.area_chart(df)

