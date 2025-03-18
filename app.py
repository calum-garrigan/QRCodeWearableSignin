import streamlit as st
import qrcode
from io import BytesIO
from urllib.parse import urlencode

# ✅ Update this with your live Streamlit URL
STREAMLIT_APP_URL = "https://gsqi4sxeux8pwrmqyzuuwv.streamlit.app/login"

# Function to generate the QR login URL
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

# Sample accounts (can be replaced with actual data)
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
    st.markdown(f"[Direct Login Link]({login_url})")  # Fallback if QR scanning fails
