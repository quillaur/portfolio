import streamlit as st
from navigation.classes_nav import ClassesNav
from pages.courses import courses_global, python_basics, python_data_handling, python_oop

def app():
    st.title("Courses")
    app = ClassesNav()
    app.add_page("Global", courses_global.app)
    app.add_page("Python Basics", python_basics.app)
    app.add_page("Python Data handling", python_data_handling.app)
    app.add_page("Python OOP", python_oop.app)
    app.run()

    