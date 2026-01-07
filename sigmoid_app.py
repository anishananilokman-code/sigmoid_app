import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title of the application
st.title('Sigmoid Activation Function Visualization')

# Input range for the plot
x = np.linspace(-10, 10, 100)
y = 1 / (1 + np.exp(-x))

# Plotting Sigmoid function
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('Sigmoid(x)')
plt.title('Sigmoid Activation Function')
st.pyplot(plt)
