import streamlit as st

st.title("Word Counter")

uin = st.text_input("Enter text here:")
uout = 0

for i in range(len(uin.split(" "))):
	if uin.split(" ")[i] != "-" and uin.split(" ")[i] != ".":
		uout += 1

if uin != "":
	if uout == 1:
		st.write(f"This message is {uout} word long.")
	else:
		st.write(f"This message is {uout} words long.")
