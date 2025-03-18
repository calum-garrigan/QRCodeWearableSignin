import streamlit as st
from urllib.parse import parse_qs, urlparse

# Extract email and password from the URL parameters
query_params = parse_qs(urlparse(st.query_params).query)
email = query_params.get("email", [""])[0]
password = query_params.get("password", [""])[0]

st.title("Logging into Oura...")

if email and password:
    # ✅ Inject JavaScript to fill in login fields
    login_script = f"""
    <script>
        setTimeout(() => {{
            var emailField = document.querySelector("input[name='email']");
            var passwordField = document.querySelector("input[name='password']");
            if (emailField && passwordField) {{
                emailField.value = "{email}";
                passwordField.value = "{password}";
                console.log("✅ Auto-filled credentials!");
            }} else {{
                console.log("❌ Login fields not found!");
            }}
        }}, 2000);
    </script>
    <p>Redirecting to Oura Login...</p>
    <meta http-equiv="refresh" content="2; URL='https://cloud.ouraring.com/user/sign-in?next=%2F'" />
    """
    st.markdown(login_script, unsafe_allow_html=True)
else:
    st.error("Invalid login credentials. Please try again.")
