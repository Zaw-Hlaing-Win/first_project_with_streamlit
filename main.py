import streamlit as st
import pandas as pd
import numpy as np

usd = st.number_input("USD :", value=1)

def exchange(usd):
	if st.button("Exchange"):
		mmk = usd * 1777
		st.write("MMK :",mmk)

exchange(usd)

