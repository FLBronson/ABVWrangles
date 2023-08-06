import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

usFile = pd.read_csv('https://raw.githubusercontent.com/FLBronson/ABVWrangles/main/data.csv')

st.title('Data')

state = st.selectbox('Select a State', usFile['State'].unique())

state_data = usFile[usFile['State'] == state]

st.header('Info about the state')
st.write(state_data)

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(usFile['State'], usFile['LILATracts_1And10'], color='g', alpha=0.5)
ax.bar(state_data['State'], state_data['LILATracts_1And10'], color='r')
plt.xlabel('State')
plt.ylabel('Food Desert?')
plt.title('Food Deserts')
plt.tight_layout()

st.pyplot(fig)