import streamlit as st
import random

st.title("🔥 Şifre + Pokémon Evrim Sistemi")

uzunluk = st.number_input("Şifre uzunluğu:", min_value=1, max_value=50, value=8)

kucuk = "abcdefghijklmnopqrstuvwxyz"
buyuk = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rakam = "0123456789"
sembol = "!@#$%^&*"

tum = kucuk + buyuk + rakam + sembol

if st.button("Şifre Oluştur"):
    sifre = ""

    for i in range(uzunluk):
        sifre += random.choice(tum)

    st.write("### 🔑 Şifre:", sifre)

    # puan sistemi
    puan = 0
    if any(c in kucuk for c in sifre):
        puan += 1
    if any(c in buyuk for c in sifre):
        puan += 1
    if any(c in rakam for c in sifre):
        puan += 1
    if any(c in sembol for c in sifre):
        puan += 1
    if len(sifre) >= 8:
        puan += 1

    # EVRİM + BOYUT
    if puan <= 2:
        st.write("🔴 ZAYIF - Charmander")
        st.image("https://img.pokemondb.net/artwork/charmander.jpg", width=120)

    elif puan == 3:
        st.write("🟠 ORTA - Charmeleon")
        st.image("https://img.pokemondb.net/artwork/charmeleon.jpg", width=180)

    elif puan == 4:
        st.write("🟡 GÜÇLÜ - Charizard")
        st.image("https://img.pokemondb.net/artwork/charizard.jpg", width=240)

    else:
        st.write("🟢 ÇOK GÜÇLÜ - Mega Charizard")
        st.image("https://img.pokemondb.net/artwork/charizard-mega-x.jpg", width=320)