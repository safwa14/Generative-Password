import streamlit as st
import random
import string

# 🎨 تنسيق CSS حسب طلبك بالضبط
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://image.freepik.com/free-vector/purple-lock-with-key_23-2149479577.jpg");
        background-size: auto 100%;
        background-position: right center;
        background-repeat: no-repeat;
        color: white;
    }
    .block-container {
        background-color: rgba(0, 0, 0, 0.6);
        padding: 2rem;
        border-radius: 15px;
        max-width: 600px;
        margin: 100px auto;
    }
    h1 {
        color: white;
        font-size: 34px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    label, .stNumberInput label {
        color: white;
        font-size: 18px;
        font-weight: 500;
    }
    .stButton > button {
        background-color: #dcd3ff;
        color: black;
        font-size: 16px;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
        margin-top: 10px;
    }
    .stButton > button:active {
        background-color: #6f42c1;
        color: white;
    }
    .stSuccess {
        font-size: 20px;
        color: white;
        background-color: rgba(255, 255, 255, 0.1);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
        letter-spacing: 1px;
    }
    </style>
""", unsafe_allow_html=True)

# 🧠 واجهة التطبيق
st.title("🔐 Password Generator")
st.write("Welcome to the Password Generator!")

length_of_word = int(st.number_input("Enter the total number of characters in the password:", min_value=1))
length_of_litters = int(st.number_input("Enter the number of letters in the password:", min_value=0))
length_of_numbers = int(st.number_input("Enter the number of numbers in the password:", min_value=0))
length_of_symbols = int(st.number_input("Enter the number of symbols in the password:", min_value=0))

if st.button("Generate Password"):
    total = length_of_litters + length_of_numbers + length_of_symbols
    if total != length_of_word:
        st.error("Invaild input. The sum of letters, numbers, and symbols doesn't match the password length!")
    else:
        letters = random.choices(string.ascii_letters, k=length_of_litters)
        numbers = random.choices(string.digits, k=length_of_numbers)
        symbols = random.choices(string.punctuation, k=length_of_symbols)

        all_chars = letters + numbers + symbols
        random.shuffle(all_chars)
        password = ''.join(all_chars)

        st.success(f"Generated Password: {password}")