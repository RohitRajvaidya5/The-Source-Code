# AIzaSyAmhlPQ7QAF__KfgMMIy5G7otclyEWPUN0

import google.generativeai as genai
import os

# --- IMPORTANT: Set your API Key ---
# Option 1: Set as an environment variable (recommended for security)
# Before running your script, in your terminal:
# export GOOGLE_API_KEY="YOUR_API_KEY"
# (On Windows, use: set GOOGLE_API_KEY=YOUR_API_KEY)
# Then in your Python code:
# api_key = os.getenv("GOOGLE_API_KEY")
api_key = "AIzaSyAmhlPQ7QAF__KfgMMIy5G7otclyEWPUN0"
# Option 2: Directly hardcode (not recommended for production)
# api_key = "YOUR_API_KEY" # Replace with your actual API key

if not api_key:
    print("Error: Google API Key not found.")
    print("Please set the GOOGLE_API_KEY environment variable or replace 'YOUR_API_KEY' in the code.")
    exit()

genai.configure(api_key=api_key)

# Initialize the Generative Model
# You can choose different models like 'gemini-pro', 'gemini-1.5-pro-latest', etc.
# For basic text generation, 'gemini-pro' is a good starting point.
model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(user_input):
    """
    Sends user input to the Gemini model and returns the model's text response.
    """
    try:
        # For a simple text input and output, we can use generate_content
        # The model will try to complete or respond to the given input.
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    print("Gemini API Basic Interaction")
    print("Type 'exit' or 'quit' to end the conversation.")

    while True:
        user_prompt = input("You: ")
        if user_prompt.lower() in ['exit', 'quit']:
            break

        gemini_output = get_gemini_response(user_prompt)
        print(f"Gemini: {gemini_output}")