import streamlit as st
import math

st.set_page_config(
        page_title="Header Separator",
        page_icon="📃",
        layout = 'wide'
    )
# Make page content larger (zoom)
st.markdown("""<style>body {zoom: 1.1;  /* Adjust this value as needed */}</style>""", unsafe_allow_html=True)

st.title('Header Separator 🔍')

st.sidebar.success("Select a tool above.")

def separate_text_by_headers(text):
    separated_text = {}
    lines = text.split("\n")
    current_header = None
    current_text = []

    for line in lines:
        if line.strip() != "":
            if line.endswith("::"):
                # If the line ends with "::", it's a header
                if current_header is not None:
                    # If there's already text under the previous header, save it
                    separated_text[current_header] = "\n".join(current_text)
                    current_text = []

                current_header = line.strip()
            else:
                # If it's not a header, add it to the current text
                current_text.append(line)

    # Save the text under the last header
    if current_header is not None:
        separated_text[current_header] = "\n".join(current_text)

    return separated_text

col1,col2 = st.columns(2)

with col1:
    text = st.text_area(label = ':red[Please enter any text to separate by headers ending in ::]',placeholder = 'Input text here',height = 500)
    if text is not None:
        separated_text = separate_text_by_headers(text)
        selected_header = st.selectbox(label = 'Headers:',options = separated_text.keys())
    
with col2:
    if selected_header is not None:
        text2 = st.text_area(label = ':green[Here is your text under the selected header:]',placeholder = 'Output text here',value = separated_text[selected_header],height = 500)