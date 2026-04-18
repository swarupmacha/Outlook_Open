import streamlit as st
import urllib.parse

st.title("Outlook Email Sender")

subject = "Daily Job Status Report"
body = "Hi Team,\n\nAll jobs are running fine.\n\nRegards,\nSwarup"

mailto_link = f"mailto:?subject={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}"

if st.button("Send Email"):
    st.markdown(
        f'<meta http-equiv="refresh" content="0; url={mailto_link}">',
        unsafe_allow_html=True
    )
