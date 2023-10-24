import streamlit as st

st.title("Word Counter")

uin = st.text_input("Enter text here:").split(" ")
uout = 0

for i in range(len(uin)):
	if uin[i] not in [":", ";", ".", ",", "-", "+", "*"]:
		ulst = list(uin[i])
		ulst.pop(" ")
		uin[i] = ulst
		
if uin != "":
	if uout == 1:
		st.write(f"This message is {uout} word long.")
	else:
		st.write(f"This message is {uout} words long.")
