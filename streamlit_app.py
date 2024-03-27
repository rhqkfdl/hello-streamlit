import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

rand = np.random(np.random.normal(1,2,size=20))
fig, ab = plt.subplots()
ab.hist(rand,bins = 15)
st.pyplot(fig)