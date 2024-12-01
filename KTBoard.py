import streamlit as st

st.title('Kill Team SCOREBOARD')

score_party1_critical = 0
score_party1_kill = 0
score_party1_secret = 0


print("ergebnis:")
print(score_party1_critical)



points = ["Critical", "Kill", "Secret"]
selection = st.pills("Scored for", points, selection_mode="single")


##if selection in ["Critical"]:

score_party1_critical = score_party1_critical +1
##else:
##    print("nix")




