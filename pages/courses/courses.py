import streamlit as st
import pandas as pd
from PIL import Image
from collections import defaultdict

# from navigation.courses_nav import CoursesNav
# from pages.courses import courses_global, python_courses
# from utilities import pretty_bar_plot

def app():
    st.title("Courses")
    # app = CoursesNav()
    # app.add_page("Global", courses_global.app)
    # app.add_page("Python", python_courses.app)
    # app.run()

    # Filter activities by concept wanted.
    df = pd.read_csv("data/courses.csv", sep=",")

    available_course = ["Global"] + df["Course"].unique().tolist()

    course = st.selectbox("Select the course:", available_course)

    if course == "Global":
        st.info("Here is what I can teach.")
        teachings = Image.open("images/teachings.png")
        st.image(teachings)
    
    else:
        df = df[df["Course"] == course]

        concepts = df["Concept"].unique()
        wanted_concepts = st.multiselect("Concept(s):", concepts, default=concepts)

        df = df[df["Concept"].isin(wanted_concepts)]

        selected_activities = df["Activity"].unique()

        matched_concepts = defaultdict(list)
        for activity in selected_activities:
            # matched_concepts["Activity"].append(activity)

            tmp_df = df[df["Activity"] == activity]

            total = 0
            for concept in concepts:
                if any(tmp_df["Concept"] == concept):
                    matched_concepts[concept].append("Yes")
                    total += 1
                else:
                    matched_concepts[concept].append("No")
            
            matched_concepts["Total"].append(total)

        def bg_colour_col (col):
            colour = '#ffff00'
            return ['background-color: %s' % colour if x == "Yes" else "" for i,x in col.iteritems()]
        
        st.dataframe(pd.DataFrame(matched_concepts, index=selected_activities).sort_values(by=["Total"], ascending=False).style.apply(bg_colour_col))

        st.subheader(f"""
                    Link to the {course} activities :
                """)
        github_repo_url = "https://github.com/quillaur/apprendre_python/"

        links = {
            "Quizz game": "tree/main/quizz",
            "Guess the number": "tree/main/devine_le_chiffre",
            "Rock / Paper / Scisors": "blob/main/pierre_ciseaux_papier/pierre_ciseaux_papier.py",
            "Mendel genetics": "tree/main/genetique_mendel",
            "Password manager": "tree/main/cryptographie",
            "Weather prediction": "blob/main/weather/weather_api.py",
            "Currency exchange": "tree/main/taux_echange_devise"
        }

        msg = ""
        for activity in selected_activities:
            msg += f"* [{activity}]({github_repo_url}{links[activity]})\n"
        st.markdown(msg, unsafe_allow_html=True)
