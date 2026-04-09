import streamlit as st
from model import predict_stress

st.title("🧠 Mental Stress Detection System")

sleep = st.slider("Sleep Hours", 0, 12, 6)
screen = st.slider("Screen Time (hours)", 0, 12, 5)
work = st.slider("Work/Study Hours", 0, 12, 6)
mood = st.slider("Mood (1-10)", 1, 10, 5)
activity = st.slider("Physical Activity (hours)", 0, 5, 2)

if st.button("Predict Stress"):
    result = predict_stress([sleep, screen, work, mood, activity])
    
    st.subheader(f"Stress Level: {result}")

    st.write("### Suggestions:")

    if sleep < 6:
        st.write("- Increase sleep duration")
    if screen > 6:
        st.write("- Reduce screen time")
    if work > 8:
        st.write("- Take breaks")
    if activity < 2:
        st.write("- Do exercise")
    if mood < 5:
        st.write("- Try meditation")