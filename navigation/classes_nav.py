import streamlit as st

from navigation.multipage import MultiPage

class ClassesNav(MultiPage):

    def run(self):
        # Overwrite the run function to get as many buttons as wanted.
        col1, col2 = st.columns([1,5])
        with col1:
            button = st.selectbox("", self.pages, format_func=lambda x: x["title"])
        
        with col2:
            # run the app function 
            button['function']()