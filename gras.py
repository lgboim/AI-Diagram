import streamlit as st
import os
import subprocess
import re
from groq import Groq  # Import the Groq library

def sanitize_filename(input_str):
    filename = re.sub(r'\s+', '_', input_str)
    filename = re.sub(r'[^\w\-_]', '', filename)
    filename = filename[:50]  # Limit the filename length
    return filename

def get_graphviz_code_from_groq(user_input):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Based on {user_input}, Generate only the Python code for a concise Graphviz diagram with logical multiple connections and relevant Layout Engines. Do not write any text other than the code. Do not write '%Nodes' or '% Sensory' or any titles in the code, use just '_', not '-'. maximum 150 dots. all of it is very impertant!.",
            }
        ],
        model="llama2-70b-4096",  # Use the appropriate model
    )

    graphviz_code = re.sub(r".*```\n(.*?)\n```.*", r"\1", chat_completion.choices[0].message.content, flags=re.DOTALL)
    return graphviz_code

def generate_diagram(graphviz_code, filename):
    dot_filename = f'{filename}.dot'
    png_filename = f'{filename}.png'
    try:
        with open(dot_filename, 'w') as file:
            file.write(graphviz_code)
        subprocess.run(['dot', '-Tpng', dot_filename, '-o', png_filename], check=True)
        return png_filename
    except Exception as e:
        st.error(f"Error generating diagram: {e}")
        return None

st.title("Graphviz Diagram Generator with Groq API")

user_input = st.text_area("Enter your architecture description:", height=150)

if st.button("Generate Diagram"):
    if len(user_input) < 10:
        st.warning("Description should be at least 10 characters long.")
    else:
        filename = sanitize_filename(user_input)
        graphviz_code = get_graphviz_code_from_groq(user_input)
        if graphviz_code:
            png_filename = generate_diagram(graphviz_code, filename)
            if png_filename:
                st.image(png_filename, caption="Generated Diagram")
                st.code(graphviz_code, language='python')
        else:
            st.error("Failed to generate code from the API.")

