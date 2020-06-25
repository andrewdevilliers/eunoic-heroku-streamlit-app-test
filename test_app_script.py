import streamlit as st

st.title("This is a test")
number_1 = st.text_input("First number: ")
number_2 = st.text_input("Second number: ")
result = number_1 + number_2
st.write("The sum of your numbers is: " + result)
