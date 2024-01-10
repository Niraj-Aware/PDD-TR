pip install --upgrade streamlit

import streamlit as st

def main():
    st.title("Website Redirect Buttons")

    # Create two buttons side by side
    col1, col2 = st.beta_columns(2)

    if col1.button("Veg Plant"):
        # Define the URL for Website 1
        website_url_1 = "https://www.example.com"
        # Open the website in a new tab
        st.markdown(f"[Website 1]({website_url_1})", unsafe_allow_html=True)

    if col2.button("Cash Crop"):
        # Define the URL for Website 2
        website_url_2 = "https://www.example2.com"
        # Open the website in a new tab
        st.markdown(f"[Website 2]({website_url_2})", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
