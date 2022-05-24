import streamlit as st
from navigation.courses_nav import CoursesNav
from pages.courses import courses_global, python_courses

def app():
    st.title("Courses")
    app = CoursesNav()
    app.add_page("Global", courses_global.app)
    app.add_page("Python", python_courses.app)
    app.run()

    