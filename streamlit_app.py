import streamlit as st

st.set_page_config(page_title="Spiff's Result Checker", page_icon="🎓")

st.title("🎓 STUDENT RESULT CHECKER")
st.write("Built by Spiff - Future Software Engineer")
st.divider()

name = st.text_input("Enter Student Name")
score = st.number_input("Enter Score (0-100)", min_value=0, max_value=100, step=1)

if st.button("Check Result", use_container_width=True):
    if not name:
        st.warning("Please enter a name first!")
    else:
        st.divider()
        st.subheader(f"Result for {name}: {score}")
        if score >= 70:
            st.success(f"Grade: A - Excellent! 🌟")
            st.balloons()
        elif score >= 60:
            st.success(f"Grade: B - Very Good! 👍")
        elif score >= 50:
            st.info(f"Grade: C - Good")
        elif score >= 40:
            st.info(f"Grade: D - Pass")
        else:
            st.error(f"Grade: F - Fail, need to retake 😔")

st.divider()
st.caption("Day 1 Project - Built on phone | Agbor, Delta")
