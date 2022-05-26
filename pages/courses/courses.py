from operator import sub
import streamlit as st
import pandas as pd
from PIL import Image
from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles
import numpy as np

# from navigation.courses_nav import CoursesNav
# from pages.courses import courses_global, python_courses
# from utilities import pretty_bar_plot

def app():
    st.title("Courses")

    # Load activities.
    df = pd.read_csv("data/courses.csv", sep=",")
    available_course = ["Global"] + df["Course"].unique().tolist()
    course = st.selectbox("Select the course:", available_course)
            
    #######################
    ### The Global page ###
    #######################
    if course == "Global":

        col1, col2 = st.columns([2,1])
        with col1:
            teachings = Image.open("images/teachings.png")
            st.image(teachings)

        with col2:
            sub_sets = {}
            labels = ["Python", "Data Science", "Dynamic Programming"]
            for c in labels:
                filtered = df[df["Course"] == c]
                sub_sets[c] = list(filtered["Concept"].unique())

            # All python concepts should be included in DS and DP
            for k, v in sub_sets.items():
                if k != "Python":
                    sub_sets[k] = v + sub_sets["Python"]
            
            # Remove python as it is common to both DS and DP.
            del sub_sets["Python"]
            del labels[0]

            fig = plt.figure(figsize=(3,3))
            sub_sets = [set(v) for k,v in sub_sets.items()]
            colors = ("darkorange", "darkgreen")
            v = venn2(sub_sets, set_labels = set(labels), set_colors=colors, alpha=0.4)
            
            # Outside circles labels.
            for i, text in enumerate(v.set_labels):
                if text:
                    text.set_color(colors[i])
            
            # Inside circles labels.
            for text in v.subset_labels:
                if text:
                    text.set_text("")

            # add outline
            venn2_circles(sub_sets, linestyle="dashed", linewidth=1)

            fig.patch.set_alpha(0.0)
            fig.text(0.5, 0.5, "Python", ha='center', va='center', fontsize=12, color="blue")

            st.pyplot(fig)

        st.subheader(f"Trusted by:")
        schools = Image.open(f"images/{course.lower()}_schools.png")
        # schools.thumbnail((500, 300), Image.ANTIALIAS)
        st.image(schools)
    
    else:
        #######################
        ### The other pages ###
        #######################

        # Filter activities by concepts
        # The multiselect button

        col1, col2, col3 = st.columns([3,0.2,1])
        df = df[df["Course"] == course]
        concepts = df["Concept"].unique()

        with col1:
            wanted_concepts = st.multiselect("You can filter activities by concept(s):", concepts, default=concepts)

            if wanted_concepts:
                #################################
                # The dataframe with activities #
                #################################
                df_filtered_concepts = df[df["Concept"].isin(wanted_concepts)]
                selected_activities = df_filtered_concepts["Activity"].unique()

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

                with col3:
                    #################################
                    #### The list of activities #####
                    #################################
                    st.subheader(f"""
                                Links to the {course} activities :
                            """)
                    github_repo_url = "https://github.com/quillaur/apprendre_python/"
                    msg = ""
                    df_filtered_activities = df[df["Activity"].isin(selected_activities)]
                    df_filtered_activities = df_filtered_activities[["Activity", "Link"]].drop_duplicates()
                    for i, row in df_filtered_activities.iterrows():
                        if row['Link'] is not np.nan:
                            msg += f"* [{row['Activity']}]({github_repo_url}{row['Link']})\n"
                        else:
                            msg += f"* {row['Activity']}\n"
                    st.markdown(msg, unsafe_allow_html=True)

                #####################
                #### The schools ####
                #####################
                st.subheader(f"This {course} course is trusted by:")
                schools = Image.open(f"images/{course.lower()}_schools.png")
                schools.thumbnail((500, 300), Image.ANTIALIAS)
                st.image(schools)