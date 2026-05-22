import streamlit as st
import ollama
from PIL import Image

st.set_page_config(
    page_title="Image OCR",
    layout="wide",
    initial_sidebar_state="auto"
)

st.title("Llama OCR")

col1, col2 = st.columns([6,1])
with col2:
    if st.button("Clear Image"):
        if 'ocr_result' in st.session_state:
            del st.session_state['ocr_result']
        st.rerun()

st.text("Extract structured text from images using Llama 3.2 Vision!")

with st.sidebar:
    st.header("Upload Image")
    uploaded_file = st.file_uploader("Choose an image...",type=["png","jpg","jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image,caption="Uploaded Image")

        if st.button("Extract text"):
            with st.spinner("Processing..."):
                try:
                    response = ollama.chat(
                                    model='llama3.2-vision:11b',
                                    messages=[
                                        {
                                        'role': 'user',
                                        'content': """Analyze the text in the provided image. Extract all readable content
                                        and present it in a structured Markdown format that is clear, concise, 
                                        and well-organized. Ensure proper formatting (e.g., headings, lists, or
                                        code blocks) as necessary to represent the content effectively.""",
                                        'images': [uploaded_file.getvalue()]
                                        }
                                    ],
                                    )
                    st.session_state['ocr_result']=response.message.content
                except Exception as e:
                    st.error(f"Error processing image: {str(e)}")

if 'ocr_result' in st.session_state:
    st.markdown(st.session_state['ocr_result'])
else:
    st.info("Upload an image and click 'Extract Text' to see the results here")