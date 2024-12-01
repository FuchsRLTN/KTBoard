import streamlit as st

st.title('Kill Team SCOREBOARD')




points = ["Critical", "Kill", "Secret"]
selection = st.pills("Scoerd for", options, selection_mode="multi")
st.markdown(f"Your selected options: {selection}.")

