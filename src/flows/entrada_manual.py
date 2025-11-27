import streamlit as st
import pandas as pd
import os

from utils.Validación_facturas import validar_factura_individual

# Inicializa claves de estado
if "factura_manual" not in st.session_state:
    st.session_state.factura_manual = None
if "factura_valida" not in st.session_state:
    st.session_state.factura_valida = False

# Funcion principal 

def escribir_factura():
    st.subheader("Introduzca los datos de la factura")
    Numero_Factura = st.text_input("Número de la factura: ")
    Fecha = st.text_input("Fecha de emisión: (Formato --> Año_Mes_Día)")
    cliente = st.text_input("Detalles del cliente:")
    vendedor = st.text_input("Detalles del vendedor:")
    descripcion = st.text_area("Descripción de los productos o servicios:")
    precio = st.text_input("Precios de los productos o servicios: (con €)")
    impuestos = st.text_input("Impuestos aplicables: (con €)")
    total = st.text_input("Total a pagar (con €)")

    # Boton para validar

    if st.button("Validar factura"):
        factura_manual = {
             "Número de factura": Numero_Factura,
             "Fecha de emisión": Fecha,
             "Detalles del cliente": cliente,
             "Detalles del vendedor": vendedor,
             "Descripción de los productos o servicios": descripcion,
             "Precios de los productos o servicios": precio,
             "Impuestos aplicables": impuestos,
             "Total a pagar": total
             }
        
        es_valida, errores = validar_factura_individual(factura_manual)
        st.session_state.factura_manual = factura_manual
        st.session_state.factura_valida = es_valida

        if es_valida:
            st.success("✅ Factura válida")

        else:
            st.error("❌ Factura inválida:")
            for error in errores:
                st.write(f"- {error}")

    # Botón de guardado persistente: aparece tras validar si es válida
    if st.session_state.factura_valida and st.session_state.factura_manual:
        st.divider()
        st.info("La factura es válida. Puedes guardarla en CSV.")
        
        col_save, col_dl = st.columns([1,1])

        with col_save:
            if st.button("Guardar en CSV", key="guardar_csv"):
                df = pd.DataFrame([st.session_state.factura_manual])
                carpeta = "facturas_validas"
                os.makedirs(carpeta, exist_ok=True)
                nombre_csv = (
                    f"factura_{st.session_state.factura_manual.get('Número de factura','')}.csv"
                    if st.session_state.factura_manual.get("Número de factura")
                    else "factura_valida.csv"
                )
                ruta = os.path.join(carpeta, nombre_csv)
                df.to_csv(ruta, index=False, encoding="utf-8-sig")
                st.success(f"Factura guardada en {ruta}")
                st.write("Ruta absoluta:", os.path.abspath(ruta))

        # Botón de descarga directa en el navegador
        with col_dl:
            df = pd.DataFrame([st.session_state.factura_manual])
            st.download_button(
                label="Descargar CSV",
                data=df.to_csv(index=False, encoding="utf-8-sig"),
                file_name=(
                    f"factura_{st.session_state.factura_manual.get('Número de factura','')}.csv"
                    if st.session_state.factura_manual.get("Número de factura")
                    else "factura_valida.csv"
                ),
                mime="text/csv"
            )
