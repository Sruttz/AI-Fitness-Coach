import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure GenerativeAI API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    chat = model.start_chat(history=[])
    response = chat.send_message(question, stream=True)
    return response

# Initialize Streamlit app
st.set_page_config(page_title="Nutrition Recommendation")
st.title("Nutrition Plan")

# Input for fitness goal
goal_type = st.selectbox("Select your fitness goal:", ["Weight loss", "Muscle gain", "Endurance improvement", "Overall health and wellness"])

# Input for age
age = st.number_input("Enter your age:", min_value=10, max_value=100, step=1)

# Button to generate nutrition plan
submit_button = st.button("Generate Nutrition Plan")

# Check if input is not empty and button is clicked
if goal_type and age and submit_button:
    st.subheader("Here's the Nutrition Plan:")
    # Create prompt based on user inputs
    prompt = f"Generate a nutrition plan for {goal_type.lower()} individuals aged {age} "
    response = get_gemini_response(prompt)
    if response:
        for chunk in response:
            if hasattr(chunk, "text"):
                st.write(chunk.text)
            else:
                st.warning("Unable to generate nutrition plan. Please try again later.")
    else:
        st.warning("Unable to generate nutrition plan. Please try again later.")
