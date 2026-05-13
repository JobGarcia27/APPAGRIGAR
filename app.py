import streamlit as st

st.title("🌱 Sistema Finca Libertad")

usuario = st.text_input("Usuario")
password = st.text_input("Contraseña", type="password")

if st.button("Ingresar"):

    if usuario == "mauricio" and password == "1234":
        st.success("Bienvenido al sistema")

    else:
        st.error("Credenciales incorrectas")