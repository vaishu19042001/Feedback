import streamlit as st

st.title("Candidate Feedback")

feedback_options = {
    "Excellent": "🌟",
    "Good": "👍",
    "Average": "😐",
    "Bad": "👎",
    "Very bad": "💔"
}

# feedback selection with corresponding emojis
feedback = st.radio("Please rate your experience with us", list(feedback_options.keys()), format_func=lambda x: f"{feedback_options[x]} {x}")

st.write("-----")
comment = st.text_input('Write your message here')

# buttons for cancel and submit
if st.button('Submit'):
    # Provide specific feedback messages based on the selected rating and comment
    if feedback in ["Excellent", "Good"]:
        st.success("Thank you for your positive feedback!")
    elif feedback == "Average":
        st.info("We appreciate your feedback. We will strive to improve.")
    else:
        st.error("We're sorry to hear that. Please provide more details in the comment.")
