import streamlit as st

def mostrar_reglas():
    regla = st.selectbox(
        "Ayuda : Regla de validación",
        [
            "Número de factura válido",
            "Formato correcto de fecha",
            "Incluir cliente y vendedor",
            "Descripción",
            "Moneda",
            "Impuestos",
            "Total a pagar"])
    if regla == "Número de factura válido":
        st.info("La factura debe incluir un número de factura único, con el siguiente formato XX-XX-XXXY. Donde X es una letra e Y es un número")
    elif regla == "Formato correcto de fecha":
        st.info("La factura debe incluir la fecha de emisión en formato YYYY-MM-DD.")
    elif regla == "Incluir cliente y vendedor":
        st.info("La factura debe incluir los detalles del cliente y del vendedor." )
    elif regla == "Descripción":
        st.info("La factura debe incluir una descripción de los productos o servicios no menor a 50 caracteres.")
    elif regla == "Moneda":
        st.info("La factura debe incluir los precios de los productos o servicios en euros.")
    elif regla == "Impuestos":
        st.info("La factura debe incluir los impuestos aplicables, siempre y cuando esos impuestos no sean negativos.")
    elif regla == "Total a pagar":
        st.info("La factura debe incluir el total a pagar, que no debe ser mayor que 2000 euros.")

