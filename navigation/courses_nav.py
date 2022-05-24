import streamlit as st

from navigation.multipage import MultiPage

class CoursesNav(MultiPage):

    def run(self):
        # Overwrite the run function to get as many buttons as wanted.
        col1, col2 = st.columns([1,5])
        with col1:
            button = st.selectbox("", self.pages, format_func=lambda x: x["title"])

            if button["title"] == "Python":
                github_repo_url = "https://github.com/quillaur/apprendre_python/"
                st.markdown(f"""
                        * [Quizz game]({github_repo_url}tree/main/quizz)
                        * [Guess the number]({github_repo_url}tree/main/devine_le_chiffre)
                        * [Rock / Paper / Scisors]({github_repo_url}blob/main/pierre_ciseaux_papier/pierre_ciseaux_papier.py)
                        * [Mendel's genetics]({github_repo_url}tree/main/genetique_mendel)
                        * [Password manager]({github_repo_url}tree/main/cryptographie)
                        * [Weather prediction]({github_repo_url}blob/main/weather/weather_api.py)
                        * [Currency exchange]({github_repo_url}tree/main/taux_echange_devise)
                    """, unsafe_allow_html=True)
        
        with col2:
            # run the app function 
            button['function']()