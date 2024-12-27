import streamlit as st

st.title("BMI Calculator")

height = st.slider("Enter your hight (in cm): ", 100, 250, 170)
weight = st.slider("Enter your weight (in kg): ", 100, 200, 70)

bmi = weight / ((height / 100) ** 2)

st.write(f"Your BMI is: {bmi:.2f}")

st.subheader("BMI Categories")
st.write("- Uderweight: BMI less than 18.5")
st.write("- Normal Weight: BMI between 18.5 and 24.9")
st.write("- Overweight: BMI between 25 and 29.9")
st.write("- Obesity: BMI 30 or greater")

