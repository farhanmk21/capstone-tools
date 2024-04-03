import streamlit as st

st.set_page_config(
        page_title="Line Remover",
        page_icon="📃",
        layout = 'wide'
    )
# Make page content larger (zoom)
st.markdown("""<style>body {zoom: 1.2;  /* Adjust this value as needed */}</style>""", unsafe_allow_html=True)

st.title('Line Remover 📃')

st.sidebar.success("Select a tool above.")

col1,col2 = st.columns(2)

with col1:
    t1 = st.text_area(label = 'Please enter any text to remove extra lines from:',placeholder = 'Input text here',height = 500)


with col2:
    st.text_area(label = 'Here is your input with extra lines removed:',placeholder = 'Output text here',value = "".join([s for s in t1.splitlines(True) if s.strip('\n')]),height = 500)

