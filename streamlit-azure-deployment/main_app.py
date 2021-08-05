import streamlit as st
import pandas as pd
import app
import upload

st.set_page_config(layout="wide")

PAGES = {

	"Explore Existing Whitepapers in Database" : app,
	"Upload New Whitepaper" : upload
}


def main():

	selection = st.sidebar.radio("", list(PAGES.keys()))


	if PAGES[selection] == app:
		app.write()	

	elif PAGES[selection] == upload:
		upload.write()

if __name__ == '__main__':
	main()
