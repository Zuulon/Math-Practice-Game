import streamlit as st
import random

st.title("Math Practice Game")

with st.form("input_form"):
    difficulty = st.select_slider("Choose the level of difficulty:", options=[1, 2, 3, 4, 5])
    num_pro = st.select_slider("How many questions would you like?", options=[1, 2, 3])
    start_game = st.form_submit_button("Start Game")

if start_game:
    st.session_state.questions = []
    st.session_state.answers = []
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.is_answer_submitted = False

    def gen_questions(difficulty, num_pro):
        for i in range(num_pro):
            a = random.randint(1, 10 * difficulty)
            b = random.randint(1, 10 * difficulty)
            operator = random.choice(["+", "-", "*", "/"])
            if operator == "+":
                question = str(a) + " + " + str(b)
                correct_answer = a + b
            elif operator == "-":
                question = str(a) + " - " + str(b)
                correct_answer = a - b
            elif operator == "*":
                question = str(a) + " * " + str(b)
                correct_answer = a * b
            elif operator == "/":
                b = max(1, b)
                question = str(a) + " / " + str(b)
                correct_answer = round(a / b, 2)

            st.session_state.questions.append(question)
            st.session_state.answers.append(correct_answer)


    gen_questions(difficulty, num_pro)

if "questions" in st.session_state and "answers" in st.session_state:
    current_index = st.session_state.current_index


    if current_index < len(st.session_state.questions):
        question = st.session_state.questions[current_index]
        correct_answer = st.session_state.answers[current_index]

        st.write("Question " + str(current_index + 1) + ": " + question)

        user_answer = st.number_input(
            "Enter your answer for Question " + str(current_index + 1) + ":",
            key="current_answer",
            value=0.0,
        )

        if st.button("Submit Answer"):
            if not st.session_state.is_answer_submitted:
                if user_answer == correct_answer:
                    st.success("Correct! 🎉")
                    st.session_state.score += 1
                else:
                    st.error("Incorrect. The correct answer was " + str(correct_answer) + ".")
                st.session_state.is_answer_submitted = True

        if st.button("Next Question"):
            if st.session_state.is_answer_submitted:
                st.session_state.current_index += 1
                st.session_state.is_answer_submitted = False
            else:
                st.warning("Please submit your answer before proceeding to the next question!")
    else:
        st.write("Game Over! ")
        st.write("Your final score is: " + str(st.session_state.score) + "/" + str(len(st.session_state.questions)))
