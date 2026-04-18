---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[1], line 11
      8     webbrowser.open(mailto_link)
     10 # Example (Streamlit)
---> 11 import streamlit as st
     13 if st.button("Send Email"):
     14     open_outlook_draft()

ModuleNotFoundError: No module named 'streamlit'
