import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

usFile = pd.read_csv('https://raw.githubusercontent.com/FLBronson/ABVWrangles/main/data.csv')
flFile = pd.read_csv('https://raw.githubusercontent.com/FLBronson/ABVWrangles/main/florida.csv')
gaFile = pd.read_csv('https://raw.githubusercontent.com/FLBronson/ABVWrangles/main/georgia.csv')
alFile = pd.read_csv('https://raw.githubusercontent.com/FLBronson/ABVWrangles/main/alabama.csv')

st.set_page_config(page_title = 'Food Deserts', layout = 'wide')
st.title('Food Deserts')

tab1, tab2, tab3, tab4 = st.tabs(["United States", "Florida", "Georgia", "Alabama"])

with tab1:
    st.write(usFile)
    st.title("United States Dataset")
 
with tab2:
    st.write(flFile)
    st.title("Florida Dataset")

with tab3:
    st.write(gaFile)
    st.title("Georgia Dataset")
    
with tab4:
    st.write(alFile)
    st.title("Alabama Dataset")