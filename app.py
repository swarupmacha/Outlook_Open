import streamlit as st
import webbrowser

def open_outlook_draft():
    subject = "Daily Job Status Report"
    body = "Hi Team,\n\nThis is a test email.\n\nRegards,\nSwarup"

    mailto_link = f"mailto:?subject={subject}&body={body}"
    webbrowser.open(mailto_link)

st.title("Email Sender")

if st.button("Send Email"):
    open_outlook_draft()
