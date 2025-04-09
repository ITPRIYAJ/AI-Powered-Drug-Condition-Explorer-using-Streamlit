import streamlit as st
from utils.drug_utils import load_data
from ml.drug_recommender import DrugRecommender

# Load drug data and model
drug_data = load_data()
recommender = DrugRecommender()

st.title("💊 Drug Information System with ML")
st.markdown("Explore drugs or get recommendations based on your symptoms.")

# Static section
drug_name = st.selectbox("Select a drug:", list(drug_data.keys()))
info = drug_data[drug_name]
st.subheader(f"ℹ️ About {drug_name}")
st.write(f"**Used For:** {info['used_for']}")
st.write("**Side Effects:**")
for effect in info['side_effects']:
    st.markdown(f"- {effect}")

st.markdown("---")

# ML prediction
st.header("🤖 Drug Suggestion by Symptoms")
user_input = st.text_input("Enter your symptoms (e.g., fever headache):")

if user_input:
    suggested = recommender.predict(user_input)
    st.success(f"Suggested Drug: **{suggested}**")
