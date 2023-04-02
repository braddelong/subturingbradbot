import streamlit as st


st.set_page_config(page_title='SubTuringBradBot')
st.header('SubTuringBradBot')

st.markdown("""

	**I am a SubTuring instantiation** of the writings of 
	economist Brad DeLong, specifically his bookk _Slouching
	Towards Utopia_ and his Grasping Reality weblog on SubStack. 
	Ask me... not anything, but some things. You will see...

	"""
	)



input_text = st.text_area(label="", placeholder="Your text...")

if input_text:
	st.write(input_text)



source = "https://www.youtube.com/watch?v=U_eV8wfMkXU&t=133s"




