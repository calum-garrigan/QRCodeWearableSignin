import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from urllib.parse import parse_qs, urlparse

# Extract email and password from the URL parameters
query_params = parse_qs(urlparse(st.query_params).query)
email = query_params.get("email", [""])[0]
password = query_params.get("password", [""])[0]

st.title("Logging you in automatically...")

if email and password:
    try:
        # ✅ Set up Selenium WebDriver
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Run browser in headless mode
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(service=service, options=options)

        # ✅ Open Oura login page
        driver.get("https://cloud.ouraring.com/user/sign-in?next=%2F")

        # ✅ Fill in the email field
        email_field = driver.find_element(By.NAME, "email")
        email_field.send_keys(email)

        # ✅ Fill in the password field
        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)  # Press Enter to log in

        time.sleep(5)  # Wait for login to complete

        # ✅ Get the final logged-in page URL
        logged_in_url = driver.current_url

        # ✅ Close the Selenium browser
        driver.quit()

        # ✅ Redirect the user to their logged-in session
        redirect_script = f"""
        <meta http-equiv="refresh" content="2; URL='{logged_in_url}'" />
        <p>Successfully logged in! Redirecting...</p>
        """
        st.markdown(redirect_script, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Login failed: {str(e)}")
else:
    st.error("Invalid login credentials. Please try again.")
