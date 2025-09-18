import streamlit as st
from langchain_helper import generate_cafe_name_and_items

st.title("Cafe Name Generator")

# Cuisine selection
cuisine = st.sidebar.selectbox(
    "Pick a Cuisine",
    ["Mexican", "Italian", "Indian", "French", "American"]
)

# Vibe selection: predefined + custom
vibe_option = st.sidebar.selectbox(
    "Pick a Vibe (or choose 'Custom')",
    ["cozy", "modern", "rustic", "luxurious", "minimalist", "Custom"]
)

# If "Custom" is chosen, show a text input
if vibe_option == "Custom":
    vibe_input = st.sidebar.text_input("Enter your custom vibe")
    # ✅ fallback to "cozy" if left blank
    vibe = vibe_input if vibe_input.strip() else "cozy"
else:
    vibe = vibe_option

# Only run if both cuisine and vibe are set
if cuisine and vibe:
    response = generate_cafe_name_and_items(cuisine, vibe)

    st.header(response['cafe_name'].strip())
    st.write("### Menu Items")
    for item in response['menu_items']:
        st.write(f"- {item}")
