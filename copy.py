import streamlit as st

text_to_copy = "Hello, World!"
hosted_html_file = https://everydayswag.org/files/copy.html
iframe_url = f"{hosted_html_file }?copy={text_to_copy }"

st.markdown(f'<iframe src="{iframe_url}"></iframe>', unsafe_allow_html=True)
