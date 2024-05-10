import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import OpenAI
from pandasai.llm import AzureOpenAI
import os
import pandasai
from pandasai import Agent

#os.environ['PANDASAI_API_KEY'] = '$2a$10$KR3qAskeiFOifibYwlxkneb6AAEObfxqRoBw7yl5rxr8ij3UEY.g6'

os.environ['PANDASAI_API_KEY'] = 'sk-proj-YwNtDQkychYizOxF2fkDT3BlbkFJKubmHjpqZTvMlfMtog67'


azure_llm = AzureOpenAI(
    api_token="e8c6e6af2bff436b8adb55f7d93edcd8",
    azure_endpoint="https://prodkmnlpopenai.openai.azure.com/",
    api_version="2024-04-01-preview",
    deployment_name="GPT-35-16k"
)



def chat_with_csv(df, prompt):
    llm = OpenAI(api_token = openai_api_key)
    pandas_ai = Agent(df)
    result = pandas_ai.chat(prompt)
    print(result)
    return result

st.set_page_config(
        page_title="Chat with CSV using PandasAI",
        page_icon="📃",
        layout = 'wide'
    )
# Make page content larger (zoom)
st.markdown("""<style>body {zoom: 1.1;  /* Adjust this value as needed */}</style>""", unsafe_allow_html=True)

st.title('Chat with your CSV 🔍')

st.sidebar.success("Select a tool above.")

input_csv = st.file_uploader("Upload CSV file here.", type = ['csv'])

if input_csv is not None:
    col1, col2 = st.columns([1,1])

    with col1:
        st.info('CSV uploaded successfully')
        data = pd.read_csv(input_csv)
        st.dataframe(data)

    with col2:
        st.info('Chat with your uploaded CSV.')

        input_text = st.text_area("Enter your query.")
        if input_text is not None:
            if st.button("Chat with CSV"):
                st.info(f'Your query: {input_text}')
                sdf1 = SmartDataframe(data, config={"llm": azure_llm})
                result = sdf1.chat(input_text)
                st.success(result)
