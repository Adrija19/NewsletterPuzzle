# treasure_hunt_app.py

import streamlit as st
import webbrowser

st.set_page_config(page_title="Data Treasure Hunt", page_icon="🏴‍☠️")

st.title("🏴‍☠️ Data Treasure Hunt")
st.write("Solve all 5 questions to unlock the treasure!")

questions = [
    {"q": "Q1: What is the time complexity of binary search?", "a": "o(log n)"},
    {"q": "Q2: In SQL, what keyword combines rows from two tables based on a related column?", "a": "join"},
    {"q": "Q3: Which Python library is commonly used for data visualization starting with 'm'?", "a": "matplotlib"},
    {"q": "Q4: What does ETL stand for?", "a": "extract transform load"},
    {"q": "Q5: JSON stands for?", "a": "javascript object notation"},
]

# Session state to keep track
if 'progress' not in st.session_state:
    st.session_state.progress = 0

q_index = st.session_state.progress

if q_index < len(questions):
    current = questions[q_index]
    user_input = st.text_input(current['q']).strip().lower()

    if user_input:
        if user_input == current['a'].lower():
            st.success("✅ Correct!")
            st.session_state.progress += 1
            st.experimental_rerun()
        else:
            st.error("❌ Incorrect! Try again.")
else:
    st.balloons()
    st.success("🎉 You unlocked the treasure!")

    image_url = "https://th.bing.com/th/id/OIP.m9tKuYdDj1fuOtqbYILnjwHaD3?w=314&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7"
    st.image(image_url, caption="Submit this image to qualify!", use_column_width=True)
    st.write(f"[Click here if image doesn't load]({image_url})")