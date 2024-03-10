import streamlit as st

st.title("Candidate Feedback")

feedback_options = {
    "Excellent": "",
    "Good": "",
    "Average": "",
    "Bad": "",
    "Very bad": ""
}

# feedback selection with corresponding emojis
feedback = st.radio("Please rate your experience with us", list(feedback_options.keys()), format_func=lambda x: f"{feedback_options[x]} {x}")

st.write("-----")
comment = st.text_input('Write your message here')


# buttons for cancel and submit
if st.button('Submit'):
    st.write("Thanks for your valuable feedback!!")