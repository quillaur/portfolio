import streamlit as st
import pandas as pd

from utilities import pretty_bar_plot

def app():
    st.header("Python")

    st.info("""
                I propose to learn the basics through 7 small scripts.
                Most activities have been inspired by Tech with Tim youtube channel.
            """)
    
    # Filter activities by concept wanted.
    df = pd.read_csv("data/courses.csv", sep=";")

    concepts = df["Concept"].unique()
    wanted_concepts = st.multiselect("Concept(s):", concepts, default=concepts)

    df = df[df["Concept"].isin(wanted_concepts)]
    
    concepts_matched = df["Activity"].value_counts()
    
    # fig = pretty_bar_plot(concepts_matched, concepts_matched.index, "Number of concepts", (1,1), 8, 5)
    # st.pyplot(fig)