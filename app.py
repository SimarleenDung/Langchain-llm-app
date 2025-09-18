import streamlit as st
from langchain_helper import generate_cafe_name_and_items   # import the function

st.title("Cafe Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ["Mexican", "Italian", "Indian", "French", "American"])

if cuisine:
    response = generate_cafe_name_and_items(cuisine)

    st.header(response['cafe_name'].strip())
    menu_items = response['menu_items']   # get the menu items list
    st.write("### Menu Items")
    for item in menu_items:
        st.write(f"- {item}")
