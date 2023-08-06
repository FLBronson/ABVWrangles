import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

usFile = pd.read_csv('https://raw.githubusercontent.com/FLBronson/ABVWrangles/main/data.csv')
st.set_page_config(page_title = 'Food Deserts', layout = 'wide')

st.title('Food Deserts')
st.write(usFile)
