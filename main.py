import streamlit as st

st.title("Mi primera app")
st.write("Autor: Esta app fue elaborada por 'Woi'.")

nombre_usuario = st.text_input("Por favor, ingresa tu nombre")
mensaje_bienvenida = f"{nombre_usuario}, te doy la bienvenida a mi primera app."

st.write(mensaje_bienvenida)
