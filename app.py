import streamlit as st
from modules.db import save_user, save_session
from modules.question_loader import load_questions
from modules.evaluator import evaluate_answer
from modules.intro_generator import generate_intro
from modules.resume_parser import extract_text_from_pdf
from modules.skill_matcher import match_skills

st.set_page_config(page_title="Resume Interview Chatbot", layout="wide")

st.title("AI-Powered Resume Analyzer and Interview Preparation Chatbot")

menu = st.sidebar.selectbox(
    "Choose Module",
    ["Home", "Resume Analysis", "Interview Practice", "Self Introduction"]
)

if menu == "Home":
    st.header("User Details")
    name = st.text_input("Enter your name")
    role = st.selectbox("Select Role", ["Python Developer", "Java Developer", "HR"])

    if st.button("Save User"):
        save_user(name, role)
        st.success("User details saved successfully")

elif menu == "Resume Analysis":
    st.header("Resume Analysis")
    role = st.selectbox("Select Role for Resume Analysis", ["Python Developer", "Java Developer", "HR"])
    uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])

    if uploaded_file is not None:
        resume_text = extract_text_from_pdf(uploaded_file)
        st.subheader("Extracted Resume Text")
        st.text_area("Resume Content", resume_text, height=200)

        found, missing = match_skills(resume_text, role)

        st.subheader("Skill Analysis")
        st.write("Found Skills:", found)
        st.write("Missing Skills:", missing)

elif menu == "Interview Practice":
    st.header("Interview Practice")
    name = st.text_input("Enter your name")
    role = st.selectbox("Select Role", ["Python Developer", "Java Developer", "HR"])

    if st.button("Generate Question"):
        qdata = load_questions(role)
        st.session_state["question"] = qdata["question"]
        st.session_state["keywords"] = qdata["keywords"]

    if "question" in st.session_state:
        st.subheader("Question")
        st.write(st.session_state["question"])

        answer = st.text_area("Write your answer")

        if st.button("Evaluate Answer"):
            score, feedback = evaluate_answer(answer, st.session_state["keywords"])
            st.write("Score:", score, "/10")
            st.write("Feedback:", feedback)

            save_session(
                name,
                role,
                st.session_state["question"],
                answer,
                score,
                feedback
            )

elif menu == "Self Introduction":
    st.header("Self Introduction Generator")
    name = st.text_input("Name")
    education = st.text_input("Education")
    skills = st.text_input("Skills")
    project = st.text_input("Project")
    goal = st.text_input("Career Goal")

    if st.button("Generate Introduction"):
        intro = generate_intro(name, education, skills, project, goal)
        st.text_area("Generated Introduction", intro, height=200)