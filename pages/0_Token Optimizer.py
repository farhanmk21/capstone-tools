import streamlit as st
import math

st.set_page_config(
        page_title="Token Optimizer",
        page_icon="📃",
        layout = 'wide'
    )
# Make page content larger (zoom)
st.markdown("""<style>body {zoom: 1.1;  /* Adjust this value as needed */}</style>""", unsafe_allow_html=True)

st.title('Token Optimizer 📃')

st.sidebar.success("Select a tool above.")

#on = st.sidebar.toggle("ZERO SPACE")

on = st.checkbox("ZERO SPACE")

col1,col2 = st.columns(2)

with col1:
    t1 = st.text_area(label = ':red[Please enter any text to remove extra lines from:]',placeholder = 'Input text here',height = 500)
    len1 = len(t1)
    tok1 = len1/4
    st.text(f"{len1} characters (~{math.ceil(tok1)} tokens)")
    st.text('''Token count above is a rough estimate. 
According to OpenAI: 
1 token = ~4 characters''')

with col2:
    if on:
        t2 = st.text_area(label = ':green[Here is your input with extra lines removed:]',placeholder = 'Output text here',value = "".join([s for s in t1.splitlines(True) if s.strip()]),height = 500)
    else:
        t2 = st.text_area(label = ':green[Here is your input with extra lines removed:]',placeholder = 'Output text here',value = "".join([s for s in t1.splitlines(True) if s.strip('\n')]),height = 500)
    len2 = len(t2)
    tok2 = len2/4    
    st.text(f"{len2} characters (~{math.ceil(tok2)} tokens)")
    st.text('''Token count above is a rough estimate. 
According to OpenAI: 
1 token = ~4 characters''')
