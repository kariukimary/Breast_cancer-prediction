import streamlit as st
import mysql.connector
from mysql.connector import connect
from streamlit_extras.switch_page_button import switch_page

# Function to connect to MySQL database
def connect_to_database():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="new_password",
        database="streamlit_login"
    )
    return conn

# Function to authenticate user
def authenticate_user(username, password):
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        query = "SELECT * FROM logins WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result is not None
    else:
        return False

# Function to sign up new user
def sign_up_user(username, password):
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        query = "INSERT INTO logins (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    else:
        return False

# Streamlit login page
def main():
    st.title("Login Page")
    username_login = st.text_input("Login Username")
    password_login = st.text_input("Login Password", type="password")
    if st.button("Login"):
        if authenticate_user(username_login, password_login):
            switch_page('diagnose')
            # Redirect to dashboard or desired page after successful login
        else:
            st.error("Invalid username or password")

    st.title("Sign Up")
    with st.expander("New User? Sign Up Here"):
        username_signup = st.text_input("Sign Up Username")
        password_signup = st.text_input("Sign Up Password", type="password")
        if st.button("Sign Up"):
            if sign_up_user(username_signup, password_signup):
                switch_page('diagnose')
            else:
                st.error("Sign up failed. Please try again.")

if __name__ == "__main__":
    main()
