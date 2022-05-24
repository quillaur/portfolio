import streamlit as st

from navigation.multipage import MultiPage

class NavButtons(MultiPage):

    def run(self):
        # Overwrite the run function to get as many buttons as wanted.
        button = st.sidebar.radio("___________________________________________", self.pages, format_func=lambda x: x["title"])
        
        # run the app function 
        button['function']()