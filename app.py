import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.title("Hi, This is Narsimha")


btn_click = st.button("Don't click me!")

if btn_click == True:
    st.subheader("I said don't click me  :skull_and_crossbones:")
    st.balloons()



uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.write(df)

  # matplotlib code
  fig, ax = plt.subplots()
  df.hist(
    bins=8,
    column="Age",
    grid=False,
    figsize=(8, 8),
    color="#86bf91",
    zorder=2,
    rwidth=0.9,
    ax=ax,
  )
  st.write(fig)