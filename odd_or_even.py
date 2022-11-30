import streamlit as st
st.title('Tools for Data Science')
st.subheader('Let us see if a number is ODD or Even')
placeholder_number = st.empty()
n = placeholder_number.number_input('Please enter a number: ')
if float(n)%2 == 0:
	st.write('This is an EVEN Number')
  else:
    st.write('This is an ODD Number')
