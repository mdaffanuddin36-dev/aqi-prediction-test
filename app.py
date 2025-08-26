import streamlit as st
import pickle
import numpy as np

# Load the Random Forest Classifier model
filename = 'randomforest.pkl'
classifier = pickle.load(open(filename, 'rb'))

st.title('Air Quality Index')

# Input form
t = st.number_input('Temperature (°C)', min_value=-10.0, max_value=40.0, value=20.0)
tm = st.number_input('Maximum Temperature (°C)', min_value=-10.0, max_value=40.0, value=25.0)
tmm = st.number_input('Minimum Temperature (°C)', min_value=-10.0, max_value=40.0, value=15.0)
slp = st.number_input('Sea Level Pressure (hPa)', min_value=0.0, max_value=1200.0, value=1010.0)
h = st.number_input('Relative Humidity (%)', min_value=0, max_value=100, value=50)
vv = st.number_input('Visibility (km)', min_value=0.0, max_value=100.0, value=10.0)
v = st.number_input('Wind Speed (km/h)', min_value=0.0, max_value=50.0, value=10.0)
vm = st.number_input('Max Wind Speed (km/h)', min_value=0.0, max_value=50.0, value=15.0)

# Predict button
if st.button('Predict'):
    data = np.array([[t, tm, tmm, slp, h, vv, v, vm]])
    prediction = classifier.predict(data)
    st.write(f"The AQI for Bangalore is: {prediction[0]}")
