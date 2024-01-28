import streamlit as st
import numpy as np
import cv2

st.title('CV1 DETECTION')

uploaded_file = st.file_uploader("이미지 파일을 업로드하세요.", type=['jpg', 'jpeg', 'png'])

before, btn, after = st.columns([2,1,2])

with before:
    st.title("here is before image")
    
with btn:
    st.button("Detect")

with after:
    st.title("here is after image")


if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    
    with before:
        st.image(image, channels="BGR", caption="before image")
    

