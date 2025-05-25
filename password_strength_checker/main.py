# password_strength_meter_app.py

import streamlit as st
import re
import random
import string

# --- Password Strength Function ---
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Uppercase and Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Common Password Blacklist
    common_passwords = ["password", "123456", "password123", "qwerty", "admin", "letmein"]
    if password.lower() in common_passwords:
        feedback.append("❌ Avoid using commonly known passwords.")
        score = 1  # override score

    return score, feedback

# --- Password Generator ---
def generate_strong_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

# --- Streamlit App ---
st.title("🔐 Password Strength Meter")
st.write("Check how secure your password is and get suggestions to improve it.")

password = st.text_input("Enter your password", type="password")

if password:
    score, feedback = check_password_strength(password)

    st.markdown("### 🧠 Feedback")
    for item in feedback:
        st.write(item)

    st.markdown("### 🔍 Strength Score")
    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.warning("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.error("❌ Weak Password - Improve it using the suggestions above.")

    st.markdown("### 🎲 Generate Strong Password")
    if st.button("Suggest a Secure Password"):
        st.info(f"💡 Try this: `{generate_strong_password()}`")

else:
    st.info("👈 Please enter a password to evaluate its strength.")

