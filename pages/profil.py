import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
from datetime import datetime


def year_difference(start: str, end: str = "TODAY"):
    year, month, day = [int(x) for x in start.split()]
    start = datetime(year, month, day)

    if end == "TODAY":
        end = datetime.today()
    else:
        year, month, day = [int(x) for x in end.split()]
        end = datetime(year, month, day)
    
    return end.year - start.year

def pretty_bar_plot(x_values: list, y_values: list, x_label: str) -> plt.figure:
    # https://scentellegher.github.io/visualization/2018/10/10/beautiful-bar-plots-matplotlib.html

    # plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = 'Helvetica'
    plt.rcParams['axes.edgecolor']='#333F4B'
    plt.rcParams['axes.linewidth']=0.8
    plt.rcParams['xtick.color']='#007acc'
    plt.rcParams['ytick.color']='#007acc'

    fig, ax = plt.subplots(figsize=(3, 3))
    fig.patch.set_alpha(0.0)
    plt.hlines(y=y_values, xmin=0, xmax=x_values, color='#007acc', alpha=0.2, linewidth=5)
    plt.plot(x_values, y_values, "o", markersize=5, color='#007acc', alpha=0.6)

    # set labels style
    ax.set_xlabel(x_label, fontsize=15, fontweight='bold', color = '#007acc')
    ax.set_ylabel('')

    # change the style of the axis spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_bounds((0, len(y_values)))
    # add some space between the axis and the plot
    ax.spines['left'].set_position(('outward', 8))
    ax.spines['bottom'].set_position(('outward', 5))
    ax.patch.set_alpha(0.0)

    return fig

def app():

    col1, col2 = st.columns([2,1])
    with col1:
        st.title("Resume")
        st.info("""
                    Molecular biologist by training and data scientist by passion, 
                    I bring both these skills together to analyze your data and build the model you need to unlock the potential of your project. 
                    I have quite a bit of experience on dynamic programming coupled with statistical analysis and machine learning development projects. 
                    
                    You will find the different courses I teach as well as the projects I have achieved so far by clicking on the different sections of the left panel.
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
        fig = pretty_bar_plot(years, topics, "Years of Practice")
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
    
    # with col3:
    #     # 04 + 05/2022
    #     prices = [20]*8 + [30] + [40]*40 + [60]*15 + [75]*16 + [100]*3
    #     field = ["Mentor"]*9 + ["Mentor"]*20 + ["Evuator"]*20 + ["Teacher"]*15 + ["Data scientist"]*16 + ["Data scientist"]*3
    #     df = pd.DataFrame({"Price / hour": prices, "Job": field})
    #     fig = plt.figure(figsize=(6, 3))
    #     sns.boxplot(x = "Job", y = "Price / hour", data=df)
    #     st.pyplot(fig)
