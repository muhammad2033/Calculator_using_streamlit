import streamlit as st
from art import logo

# Function Definitions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: Division by zero!"
    return n1 / n2

def power(n1, n2):
    return n1 ** n2

# Dictionary of Operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": power
}

# Streamlit App
def main():
    st.title("Simple Calculator")
    st.image("calculator.jpeg", width=200)  # Replace "your_logo_here.png" with your logo path

    num1 = st.number_input("Enter the first number:")
    operation = st.selectbox("Select operation:", list(operations.keys()))
    num2 = st.number_input("Enter the second number:")

    if st.button("Calculate"):
        if operation in operations:
            calculation_function = operations[operation]
            try:
                result = calculation_function(num1, num2)
                st.success(f"{num1} {operation} {num2} = {result}")
            except Exception as e:
                st.error(f"Error: {str(e)}")
        else:
            st.error("Invalid operation selected.")

if __name__ == "__main__":
    main()
