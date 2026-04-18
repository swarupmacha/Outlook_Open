import streamlit as st
import win32com.client as win32

def send_from_outlook():
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)

    mail.To = "yourteam@email.com"   # optional
    mail.Subject = "Daily Job Status Report"
    mail.Body = "Hi Team,\n\nAll jobs are running fine.\n\nRegards,\nSwarup"

    # 👉 Opens Outlook draft
    mail.Display()

    # 👉 If you want auto send, use this instead:
    # mail.Send()

st.title("Outlook Mail Sender")

if st.button("Send Email"):
    send_from_outlook()
