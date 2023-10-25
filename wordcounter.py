import streamlit as st

st.title("Word Counter")

uin = st.text_input("Enter text here:")

if uin != "":
	uin = uin.split(" ")

if "\\" in uin:
	for i in range(len(uin)):

		for x in range(len(uin[i])):
		
			uin[i] = list(uin[i])
			if uin[i][x] == "\\":
				uin[i][x] = " "
			"".join(uin[i])

uout = 0

ulst = []

for i in range(len(uin)):
	
	if uin[i] not in [":", ";", ".", ",", "-", "+", "*", "!", "?", "/"]:
		for x in uin[i]:
			if x != " ":
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
