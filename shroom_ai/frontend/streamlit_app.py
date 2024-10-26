# frontend/streamlit_app.py
import streamlit as st
import requests
from PIL import Image
import io
from config import API_URL

st.title("Shroom AI")

st.header("Upload a mushroom image to determine if it's edible or not")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # When the user clicks the button, send the image to the API
    if st.button("Classify"):
        try:
            # Show spinner while processing
            with st.spinner('Analyzing mushroom...'):
                # Prepare the file for upload
                files = {"file": uploaded_file.getvalue()}
                
                # Send request to backend
                response = requests.post(f"{API_URL}/classify", files=files)
                
                # Check if request was successful
                if response.status_code == 200:
                    result = response.json()
                    edible = result.get("edible")
                    confidence = result.get("confidence", 0) * 100  # Convert to percentage
                    
                    if edible is not None:
                        if edible:
                            st.success(f"This mushroom is EDIBLE! (Confidence: {confidence:.1f}%)")
                        else:
                            st.error(f"This mushroom is NOT EDIBLE! (Confidence: {confidence:.1f}%)")
                            st.warning("⚠️ Never eat wild mushrooms without expert verification!")
                    else:
                        st.warning("Could not determine if the mushroom is edible.")
                else:
                    st.error(f"Error: {response.text}")
                    
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to the backend server. Please ensure it's running.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Add footer with warning
st.markdown("---")
st.markdown("""
⚠️ **Important Safety Warning:**
- This AI model is for educational purposes only
- Never eat wild mushrooms based solely on AI predictions
- Always consult with professional mycologists for mushroom identification
""")