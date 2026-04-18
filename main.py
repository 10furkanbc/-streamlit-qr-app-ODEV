import streamlit as st
import pyqrcode
import png

mail=st.text_input("Lütfen mail adresinizi giriniz:")
telefon="905054407855"
link=("https://wa.me/"+telefon+"?text="+mail)
qr=pyqrcode.create(link)
qr.png("wa.png",scale="12")

st.image("wa.png")

