import streamlit as st

st.title("Word Counter")

uin = st.text_input("Enter text here:")

if uin != "":
	uin = uin.split(" ")

uout = 0

for i in range(len(uin)):
	
	ulst = []
	for x in uin[i]:
		if x == "\\":
			uin[i] = " "

	if uin[i] not in [":", ";", ".", ",", "-", "+", "*", "!", "?", "/"]:
		for y in uin[i]:
			if y != " ":
				ulst.append(x)
		uin[i] = ulst

		if uin[i] != []:
			uout += 1
		
if uin != "":
	if uout == 1:
		st.write(f"This message is {uout} word long.")
	elif uout == 0:
		st.write("Please enter a valid message.")
	else:
		st.write(f"This message is {uout} words long.")
