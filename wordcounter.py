import streamlit as st

uin = st.text_input("Enter text here:")
uout = 0

for i in range(len(uin.split(" "))):
	if uin.split(" ")[i] != "-" and uin.split(" ")[i] != ".":
		uout += 1

if uin != "":
	st.write(f"Length is {uout} words.")