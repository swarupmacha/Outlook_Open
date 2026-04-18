import streamlit as st
import win32com.client as win32

# Function to create Outlook email
def create_outlook_email(subject, body, to="", cc=""):
    try:
        outlook = win32.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)

        mail.To = to
        mail.CC = cc
        mail.Subject = subject
        mail.Body = body

        mail.Display()  # Opens Outlook draft window
        return True

    except Exception as e:
        st.error(f"Error: {e}")
        return False


# Streamlit UI
st.set_page_config(page_title="Outlook Email Sender", layout="centered")

st.title("📧 Outlook Email Sender")

st.write("Create and open a draft email in Outlook")

# Input fields
to = st.text_input("To (optional)")
cc = st.text_input("CC (optional)")
subject = st.text_input("Subject", "Daily Job Status Report")

body = st.text_area(
    "Email Body",
    "Hi Team,\n\nAll jobs are running fine.\n\nRegards,\nSwarup",
    height=200
)

# Button
if st.button("Send Email"):
    success = create_outlook_email(subject, body, to, cc)

    if success:
        st.success("Outlook draft opened successfully!")
