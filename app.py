import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🏠 House Price Prediction System")

st.write("Enter details below:")

MedInc = st.number_input("Median Income")
HouseAge = st.number_input("House Age")
AveRooms = st.number_input("Average Rooms")
AveBedrms = st.number_input("Average Bedrooms")
Population = st.number_input("Population")
AveOccup = st.number_input("Average Occupancy")
Latitude = st.number_input("Latitude")
Longitude = st.number_input("Longitude")

if st.button("Predict"):
    input_data = np.array([[MedInc, HouseAge, AveRooms, AveBedrms,
                            Population, AveOccup, Latitude, Longitude]])

    prediction = model.predict(input_data)

    st.success(f"🏠 Predicted Price: {prediction[0]:.2f}")