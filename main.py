import streamlit as st
st.title('Finding greatest number among three numbers')
n1=st.number_input('Insert your first NUMBER')
n2=st.number_input('Insert your second NUMBER')
n3=st.number_input('Insert your third NUMBER')
l=[n1,n2,n3]
m=max(l)
st.write('The greatest number is',m)