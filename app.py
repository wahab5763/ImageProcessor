import os

# Create app.py only if it doesn't exist
if not os.path.exists("app.py"):
    with open("app.py", "w") as f:
        f.write("""
import streamlit as st
import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url

# Cloudinary Configuration
cloudinary.config(
    cloud_name='detwd9o8x',  # Replace with your Cloudinary cloud name
    api_key='439456689456765',  # Replace with your API key
    api_secret='tk4Ho9pJzTaTbtIcJli6JlXQkCA',  # Replace with your API secret
    secure=True
)

# Streamlit App Header
st.set_page_config(page_title="Generative Background Replacement", page_icon="🌈")
st.title("🌈 Generative Background Replacement with Cloudinary")
st.write("Upload an image and provide a prompt to transform the background using Cloudinary's generative AI.")

# Styling
st.markdown('''
    <style>
        .stFileUploader {
            padding: 20px;
            border: 2px dashed #008CBA;
            border-radius: 10px;
            text-align: center;
            background-color: #f9f9f9;
        }
        .stTextInput {
            margin-top: 20px;
        }
        .stImage {
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
    </style>
''', unsafe_allow_html=True)

# Image Upload
uploaded_file = st.file_uploader("📷 Upload an image", type=["jpg", "png", "jpeg"])

# Prompt Input
prompt = st.text_input(
    "📝 Enter a background replacement prompt",
    value="Minimalist background with a soft pastel gradient and even lighting"
)

if uploaded_file and prompt:
    # Save uploaded image to Cloudinary
    with st.spinner("Uploading image to Cloudinary..."):
        response = cloudinary.uploader.upload(uploaded_file, folder="streamlit_app")
        public_id = response["public_id"]
        st.success("Image uploaded successfully!")

    # Apply Generative Background Replace Transformation
    with st.spinner("Applying background replacement..."):
        transformed_url, options = cloudinary_url(
            public_id,
            effect=f"gen_background_replace:prompt_{prompt}"
        )
        st.success("Transformation complete!")

    # Display the Transformed Image
    st.image(transformed_url, caption="Transformed Image", use_column_width=True)

    # Provide a Download Link
    st.write(f"[Download Transformed Image]({transformed_url})")
""")
    print("app.py created.")
else:
    print("app.py already exists.")
