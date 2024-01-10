import streamlit as st
import webbrowser

def main():
    st.title("Website Redirect Buttons")

    # Create two buttons side by side
    col1, col2 = st.beta_columns(2)

    if col1.button("Vegetable Plant"):
        # Define the URL for Website 1
        website_url_1 = "https://www.example.com"
        # Open the website in a new tab
        webbrowser.open_new_tab(website_url_1)

    if col2.button("Cash Crop"):
        # Define the URL for Website 2
        website_url_2 = "https://www.example2.com"
        # Open the website in a new tab
        webbrowser.open_new_tab(website_url_2)

if __name__ == "__main__":
    main()
