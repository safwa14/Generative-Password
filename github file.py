import streamlit as st
import random
import string

# 💜 تنسيق CSS
st.markdown("""
    <style>
    .stApp {
        background-image: url('https://i.imgur.com/6yUQ7qu.jpg'); /* صورة القفل */
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: white;
    }

    .block-container {
        background-color: rgba(0, 0, 0, 0.5); /* بوكس شفاف مش فوق القفل */
        padding: 2rem;
        border-radius: 15px;
        margin-top: 100px;
    }

    h1 {
        color: white;
        font-size: 32px;
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
        background-color: #b388eb; /* موف فاتح */
        color: black; /* كلام الزر العادي */
        font-size: 16px;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
        margin-top: 10px;
    }

    .stButton > button:active {
        background-color: #5a189a !important; /* موف غامق لما تضغطي */
        color: white !important;
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

# 💬 محتوى الأبلكيشن
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