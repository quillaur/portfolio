import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
from datetime import datetime

from utilities import pretty_bar_plot


def year_difference(start: str, end: str = "TODAY"):
    year, month, day = [int(x) for x in start.split()]
    start = datetime(year, month, day)

    if end == "TODAY":
        end = datetime.today()
    else:
        year, month, day = [int(x) for x in end.split()]
        end = datetime(year, month, day)
    
    return end.year - start.year

def app():

    col1, col2 = st.columns([2,1])
    with col1:
        st.title("Resume")
        st.info("""
                    Molecular biologist by training and data scientist by passion, I bring both these skills together 
                    to analyze your data and build the model you need to unlock the potential of your project. 
                    So far, I primarily worked on classification problems as well as NLP and image processing projects.
                    Throughout my learning journey, I also acquired quite a bit of knowledge on dynamic programming using python and sometimes C++. 
                    Recently, I got to focus on training others through many teaching / mentoring missions. 
                    
                    You can find the different courses I teach as well as the projects I have achieved so far by clicking on the different sections of the left panel.
                """)
    with col2:
        profil_img =Image.open("images/profile_pict_without_bg_2.png")
        profil_img.thumbnail((400, 250), Image.ANTIALIAS)
        st.image(profil_img)
       


    col1, col2 = st.columns(2)
    
    with col1:
        experience = {
            "Data Science": year_difference("2013 1 1"),
            "Streamlit": year_difference("2021 1 1"),
            "Python": year_difference("2017 1 1"),
            "R": year_difference("2013 1 1", "2016 1 1"),
            "C++": year_difference("2017 6 1", "2019 1 1"),
            "Molecular Biology": year_difference("2012 9 1", "2018 11 18"),
            "Machine Learning": year_difference("2018 1 1"),
            "Dynamic programming": year_difference("2018 10 1")
        }

        # Sort by years of practice
        experience = {k: v for k, v in sorted(experience.items(), key=lambda item: item[1], reverse=False)}
        years = [v for k, v in experience.items()]
        topics = [k for k, v in experience.items()]
        fig = pretty_bar_plot(years, topics, "Years of Practice", (3,3), 15, 8)
        st.pyplot(fig)

    with col2:
        # 2021 + until 04/2022
        oc = 14207 + 6462
        stu = 920 + 1812.2
        epi = 8220 + 2100
        seg = 660 + 2040
        other = 2535 + 1920

        ca_parts = {
            "Teacher": stu + 0.9*epi + 0.5*seg,
            "Mentor": 0.5*oc,
            "Evaluator": 0.5*oc + 0.1*epi + 0.5*seg,
            "Data scientist": other
        }

        # create data
        fig = plt.figure(figsize=(3, 3))
        fig.patch.set_alpha(0.0)
        names = [k for k, v in ca_parts.items()]
        size = [v for k, v in ca_parts.items()]

        # Custom wedges
        explode = []
        for n in names:
            explode.append(0.2 if n == "Data scientist" else 0)
        patches, texts, autotexts = plt.pie(size, autopct="%1.f%%", labels=names, explode=explode)
        
        for text in texts:
            text.set_color("#007acc")
        for autotext in autotexts:
            autotext.set_color('white')
        st.pyplot(fig)
    
    ### Timeline TODO ####
