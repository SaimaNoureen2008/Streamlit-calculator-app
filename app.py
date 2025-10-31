import streamlit as st

# Set page title
st.set_page_config(page_title="Simple Calculator", page_icon="🧮")

# App header
st.title("🧮 Simple Calculator")
st.write("Perform basic arithmetic operations below:")

# User input fields
num1 = st.number_input("Enter first number:", value=0.0, step=1.0)
num2 = st.number_input("Enter second number:", value=0.0, step=1.0)

# Operation selection
operation = st.selectbox("Choose operation:", ["Addition", "Subtraction", "Multiplication", "Division"])

# Compute result
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"The result of addition is: {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"The result of subtraction is: {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"The result of multiplication is: {result}")
    elif operation == "Division":
        if num2 == 0:
            st.error("Division by zero is not allowed.")
        else:
            result = num1 / num2
            st.success(f"The result of division is: {result}")

# Footer
st.markdown("---")
st.caption("Created with ❤️ using Streamlit")
