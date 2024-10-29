import os
import subprocess
from pyngrok import ngrok

# Function to close existing tunnels
def close_existing_tunnels():
    try:
        # List existing tunnels
        tunnels = ngrok.get_tunnels()
        for tunnel in tunnels:
            ngrok.disconnect(tunnel.public_url)
            print(f"Closed tunnel: {tunnel.public_url}")
    except Exception as e:
        print(f"Error closing tunnels: {e}")

# Close existing tunnels if any
close_existing_tunnels()

# Create app.py only if it doesn't exist
if not os.path.exists("app.py"):
    with open("app.py", "w") as f:
        f.write("""\
import streamlit as st
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.utils import cloudinary_url

# Cloudinary Configuration
cloudinary.config(
    cloud_name='detwd9o8x',  # Replace with your Cloudinary cloud name
    api_key='439456689456765',        # Replace with your API key
    api_secret='tk4Ho9pJzTaTbtIcJli6JlXQkCA',  # Replace with your API secret
    secure=True
)

# Streamlit App
st.title("Generative Background Replacement with Cloudinary")
st.write("Upload an image and provide a prompt to transform the background using Cloudinary's generative AI.")

# Image Upload
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

# Prompt Input
prompt = st.text_input(
    "Enter a background replacement prompt",
    value="Minimalist background with a soft pastel gradient and even lighting"
)

# Add a button for the transformation
if st.button("Transform Image"):
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
        st.image(transformed_url, caption="Transformed Image")

        # Provide a Download Link
        st.write(f"[Download Transformed Image]({transformed_url})")
    else:
        st.warning("Please upload an image and enter a prompt.")
""")
    print("app.py created.")
else:
    print("app.py already exists.")

# Start the Streamlit app in the background
print("Starting Streamlit App...")
process = subprocess.Popen(['streamlit', 'run', 'app.py'])

# Create a public URL using ngrok
public_url = ngrok.connect(8501)
print(f"Streamlit app is live at: {public_url}")
