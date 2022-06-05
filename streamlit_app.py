import streamlit as st
from PIL import Image
from datetime import datetime

# Custom imports
# Multipage code from : https://github.com/prakharrathi25/data-storyteller 
from navigation.nav_buttons import NavButtons
from app_pages import profil, dashboards, courses

st.set_page_config("Porfolio", layout="wide")

with open('.streamlit/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

profil_img =Image.open("images/ai_top_mg.jpeg")
# profil_img.thumbnail((128, 128), Image.ANTIALIAS)

st.sidebar.image(profil_img)
birth = datetime(1988,4,19)
today = datetime.today()
age = today.year - birth.year

st.sidebar.header("Aurélien Quillet ~ Ph.D")
st.sidebar.info(f"""
            * {age} years old
            * Rouen, France
            * Data Scientist (remote freelance)
            * email: aurelienquillet@gmail.com
        """)

# Create an instance of the app 
# app = MultiPage()
app = NavButtons()

app.add_page("Profil", profil.app)
app.add_page("Teaching Activities", courses.app)
app.add_page("Dashboards", dashboards.app)

app.run()

st.sidebar.header("My certifications:")
st.sidebar.markdown("""
                        * [Python3](https://www.codingame.com/certification/Sf2S8q_-8pJiUwSkj8zg3w)
                        * [Algorithms](https://www.codingame.com/certification/W6KRm4XUjK51H62iW1E_mA)
                        * [Artificial Intelligence](https://www.codingame.com/certification/sgaipSY6PF5QJrpbG5isfA)
                    """, unsafe_allow_html=True)
# st.sidebar.markdown("""
#                     <div style="background-color: #f5f29a;" >
#                         <ul>
#                         <li><a href="https://www.codingame.com/certification/Sf2S8q_-8pJiUwSkj8zg3w">Python3</a></li>
#                         <li><a href="https://www.codingame.com/certification/W6KRm4XUjK51H62iW1E_mA">Algorithms</a></li>
#                         <li><a href="https://www.codingame.com/certification/sgaipSY6PF5QJrpbG5isfA">Artificial Intelligence</a></li>
#                     </div>
#                     """, unsafe_allow_html=True)

st.sidebar.header("You can follow me there:")
st.sidebar.markdown("""
                        * [Codingame](https://www.codingame.com/profile/095afbf7d889e76260103e94e4b29a5c0681142)
                        * [Linkedin](https://www.linkedin.com/in/aur%C3%A9lien-quillet-346102193/)
                        * [Github](https://github.com/quillaur)
                    """, unsafe_allow_html=True)

