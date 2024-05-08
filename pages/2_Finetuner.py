import streamlit as st
import math
import jsonlines

st.set_page_config(
        page_title="OpenAI Fine-tuner",
        page_icon="📃",
        layout = 'wide'
    )
# Make page content larger (zoom)
st.markdown("""<style>body {zoom: 1.1;  /* Adjust this value as needed */}</style>""", unsafe_allow_html=True)

st.title('Finetuner 🔍')

st.sidebar.success("Select a tool above.")

# Get prompts from the user
prompt_text = st.text_area('Enter your prompt:', height=200)
ideal_generated_text = st.text_area('Enter your ideal AI generated response:', height=200)
system_message_default = 'You are a helpful and friendly assistant.'
system_message = st.text_area('Enter your custom system message:', value=system_message_default)


if st.button('Append to output.jsonl'):
    # Format and save data to jsonl
    data = {
        "messages": [
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt_text},
            {"role": "assistant", "content": ideal_generated_text}
        ]
    }
    with jsonlines.open('output.jsonl', mode='a') as writer:
        writer.write(data)
    st.success('Data has been appended to JSONL file!')

    #st.download_button(label = "Download JSONL file", file_name='output.jsonl')


