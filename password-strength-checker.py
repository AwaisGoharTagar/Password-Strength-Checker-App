import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")

st.title("🔐Password Strength Checker")
st.markdown("""
## welcome to the ultimate password strength checker!👋
use this simple tool to check the strength of your password and get suggestions on how to make it stronger.
            we will give you helpful tips to create a **strong password** 🔒""")

password = st.text_input("Enter your password here", type="password")

feedback =[]

socre = 0

if password:
    if len(password) >= 8:
        socre += 1
    else:
        feedback.append("❌Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        socre += 1
    else:
        feedback.append("❌Password should contain both upper and lower case characters.")

    if re.search(r'\d', password):
        socre += 1
    else:
        feedback.append("❌Password should contain at least one digit.")

    if re.search(r'[!@#$%&*]', password):
        socre += 1
    else:
        feedback.append("❌Password should contain at least one special character(!, @, #, $, %, &, *).")
    if socre == 4:
        feedback.append("✅Your password is strong!🎉")
    elif socre == 3:
        feedback.append("🟡Your password is medium strength. It could be stronger.")
    else :
        feedback.append("🔴Your password is weak. Please make it stronger.")

    if feedback:
        st.markdown("## Improvement Suggestions")
        for tip in feedback:
            st.write(tip)

else:
    st.info("Please enter your password to get started.")