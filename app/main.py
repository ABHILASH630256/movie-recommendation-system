import streamlit as st

st.title("Movie Recommendation System 🎬")

st.write("Model is trained successfully!")

user_id = st.number_input("Enter User ID", min_value=1, step=1)

if st.button("Get Recommendations"):
    st.write(f"Showing recommendations for User {user_id}...")
    # You will connect your model here later
    st.success("Recommendations coming soon 🚀")