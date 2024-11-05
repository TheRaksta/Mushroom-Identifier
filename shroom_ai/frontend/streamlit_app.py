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

    # frontend/streamlit_app.py (modified section)
    if st.button("Classify"):
        try:
            with st.spinner('Analyzing mushroom...'):
                files = {"file": uploaded_file.getvalue()}
                response = requests.post(f"{API_URL}/classify", files=files)
                
                if response.status_code == 200:
                    result = response.json()
                    edible = result.get("edible")
                    confidence = result.get("confidence", 0) * 100  # Convert to percentage
                    
                    if edible is not None:
                        if edible:
                            st.success(f"This mushroom is EDIBLE! (Confidence: {confidence:.1f}%)")
                            
                            # Display species predictions if available
                            if "species_predictions" in result:
                                st.write("### Likely Species")
                                st.write(f"We are {result['species_total_confidence']*100:.1f}% confident "
                                    f"that this mushroom is one of these three species:")
                                
                                for i, pred in enumerate(result["species_predictions"], 1):
                                    species = pred["species"]
                                    conf = pred["confidence"] * 100
                                    st.write(f"{i}. {species} ({conf:.1f}% confidence)")
                                
                                st.warning("⚠️ Always verify mushroom species with an expert before consumption!")
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