import streamlit as st
import qrcode
from io import BytesIO
from urllib.parse import urlencode

# ✅ Replace with your Streamlit-hosted JavaScript auto-login page
AUTO_LOGIN_PAGE_URL = "https://gsqi4sxeux8pwrmqyzuuwv.streamlit.app/autologin"

# Function to generate the login URL
def generate_login_url(email, password):
    params = urlencode({"email": email, "password": password})
    return f"{AUTO_LOGIN_PAGE_URL}?{params}"

# Function to generate a QR code
def generate_qr_code(data):
    qr = qrcode.make(data)
    img_bytes = BytesIO()
    qr.save(img_bytes, format="PNG")
    return img_bytes.getvalue()

# Streamlit UI
st.title("Oura QR Code Auto-Login Generator")
st.write("Scan the QR code to auto-login to Oura (No typing required).")

# User inputs
email = st.text_input("Enter Oura Email", value="testuser@example.com")
password = st.text_input("Enter Oura Password", type="password")

if st.button("Generate QR Code"):
    login_url = generate_login_url(email, password)
    qr_image = generate_qr_code(login_url)

    # Show QR Code
    st.image(qr_image, caption="Scan this QR code to log in", use_container_width=True)

    # Direct link as a backup
    st.markdown(f"[Click here to log in automatically]({login_url})")
