import streamlit as st

st.title("This is a test")
number_1 = st.number_input("First number: ")
number_2 = st.number_input("Second number: ")
result = number_1 + number_2
st.write("The sum of your numbers is: ", result)

