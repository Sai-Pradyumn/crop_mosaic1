import numpy as np
import pickle
import pandas as pd
import streamlit as st

with open("crop_yield_pred.pkl", 'rb') as f:
    clf = pickle.load(f)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

def welcome():
    return "Welcome All"


def predict_crop_pred(Nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall):
    prediction = clf.predict([[Nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])
    print(prediction)
    return prediction


def main():
    html_temp = """
    <div style = "background-color:green;padding:10px">
    <h2 style="color:black;text-align:center;">Crop Yield prediction <h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    Nitrogen = st.text_input("Nitrogen")
    phosphorus = st.text_input("phosphorus")
    potassium = st.text_input("potassium")
    temperature = st.text_input("temperature")
    humidity = st.text_input("humidity")
    ph = st.text_input("ph")
    rainfall = st.text_input("rainfall")
    result = ""
    if st.button("predict"):
        result = predict_crop_pred(Nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall)
    st.success('Best crop to cultivate here - {}'.format(result))
    if st.button("About"):
        st.text("Let's Learn")
        st.text("Built with Streamlit")


if __name__ == '__main__':
    main()




