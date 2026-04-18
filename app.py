import streamlit as st
import urllib.parse

st.title("Outlook Email Sender")

subject = "24x7 Monitoring Shifts - Reminder"
body = "Hi Team,\n\nAll jobs are running fine.\n\nRegards,\nYour Name"

to = ""  # optional (leave empty or add emails)
cc = "swarup.kumar.macha@accenture.com"

mailto_link = (
    f"mailto:{to}"
    f"?subject={urllib.parse.quote(subject)}"
    f"&body={urllib.parse.quote(body)}"
    f"&cc={urllib.parse.quote(cc)}"
)

if st.button("Send Email"):
    st.markdown(
        f'<a href="{mailto_link}" target="_self">'
        f'<button style="padding:10px 20px;font-size:16px;">Open Outlook</button>'
        f'</a>',
        unsafe_allow_html=True
    )
