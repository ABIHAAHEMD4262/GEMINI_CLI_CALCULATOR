import streamlit as st
from calculator import add, subtract, multiply, divide

st.title("Simple Calculator")

num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")

operation = st.radio("Select an operation:", ("Add", "Subtract", "Multiply", "Divide"))

if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)
    
    st.success(f"The result is: {result}")
