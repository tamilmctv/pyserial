import streamlit as st
from openserial import start,end

st.title("Bill Checker")

l_col,r_col=st.columns(2)

with l_col:
    btn_start=st.button("start")
    if btn_start:
        start()


with r_col:
    btn_stop=st.button("Stop")
    if btn_stop:
        end()

