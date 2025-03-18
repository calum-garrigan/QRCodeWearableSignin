import streamlit as st
import qrcode
from io import BytesIO
from urllib.parse import urlencode

# Base URL for the Streamlit-hosted login page
STREAMLIT_APP_URL = "https://your-username-streamlit-app.streamlit.app/login"


# Function to generate a login URL
def generate_login_url(email, password):
    params = urlencode({"email": email, "password": password})
    return f"{STREAMLIT_APP_URL}?{params}"


# Function to generate a QR code
def generate_qr_code(data):
    qr = qrcode.make(data)
    img_bytes = BytesIO()
    qr.save(img_bytes, format="PNG")
    return img_bytes.getvalue()


# Streamlit UI
st.title("Oura QR Code Auto-Login Generator")
st.write("Generate QR codes for soldiers to scan and log in automatically.")

# Predefined soldier login accounts
soldier_accounts = [
    ("soldier001@ouraring.com", "Password001"),
    ("soldier002@ouraring.com", "Password002"),
    ("soldier003@ouraring.com", "Password003"),
]

# Generate QR codes for each soldier
for email, password in soldier_accounts:
    login_url = generate_login_url(email, password)
    qr_image = generate_qr_code(login_url)

    st.write(f"QR Code for {email}:")
    st.image(qr_image, caption="Scan this QR code to log in", use_column_width=False)
