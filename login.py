import streamlit as st
from urllib.parse import parse_qs, urlparse

# Extract email and password from the URL parameters
query_params = parse_qs(urlparse(st.query_params).query)
email = query_params.get("email", [""])[0]
password = query_params.get("password", [""])[0]

st.title("Logging in to Oura...")

if email and password:
    # ✅ Inject JavaScript to auto-fill and submit Oura login form
    login_script = f"""
    <script>
        setTimeout(() => {{
            let emailField = document.querySelector("input[name='email']");
            let passwordField = document.querySelector("input[name='password']");
            if (emailField && passwordField) {{
                emailField.value = "{email}";
                passwordField.value = "{password}";
                document.querySelector("button[type='submit']").click();  // Click Login Button
            }} else {{
                console.log("❌ Login fields not found!");
            }}
        }}, 3000);
    </script>
    <meta http-equiv="refresh" content="2; URL='https://cloud.ouraring.com/user/sign-in?next=%2F'" />
    <p>Auto-filling login details... Redirecting to Oura...</p>
    """
    st.markdown(login_script, unsafe_allow_html=True)
else:
    st.error("Invalid login credentials. Please try again.")
