import streamlit as st
import pandas as pd
import os

from utils.validación_facturas import validar_factura_individual

# Inicialiamos session_state para poder mantener valores persistentes y guardar el estado de las variables y así poder crear/guardar el csv 
if "factura_manual" not in st.session_state:  # Si no existe clave en factura_manual
    st.session_state.factura_manual = None    # creamos y le asignamos None, asi hay variable  disponible
if "factura_valida" not in st.session_state:
    st.session_state.factura_valida = False   # En este caso booleana para decir si es valida o no, sino hay clave por defecto la creamos con false

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

    # Botón de guardado persistente por sesion: aparece tras validar si es válida
    if st.session_state.factura_valida and st.session_state.factura_manual:
        st.divider() # visualización linea divisoria
        st.info("La factura es válida. Puedes guardarla en CSV.")
        
        col_save, col_dl = st.columns([1,1]) 

        with col_save:
            if st.button("Guardar en CSV", key="guardar_csv"):
                df = pd.DataFrame([st.session_state.factura_manual])  # movemos el diccionario gurardado en variable de sesison a un df
                carpeta = "facturas_validas"
                os.makedirs(carpeta, exist_ok=True) #creamos carpeta si no existe --> exist_ok=True evita error si ya existe
                nombre_csv = (
                    f"factura_{st.session_state.factura_manual.get('Número de factura','')}.csv" # Nombre del csv es el numero de factura
                    if st.session_state.factura_manual.get("Número de factura")
                    else "factura_valida.csv"
                )
                ruta = os.path.join(carpeta, nombre_csv)  # Creamos la ruta completa uniendo carpeta y el nombre del archivo
                df.to_csv(ruta, index=False, encoding="utf-8-sig")  # Guardadmos el df como csv en la ruta , utf-8-sig = compatiblidad excel windows
                st.success(f"Factura guardada en {ruta}")           # Mensaje de exito
                st.write("Ruta absoluta:", os.path.abspath(ruta))   # Mostramos la ruta por si acaso

        # Botón de descarga directa en el navegador
        with col_dl:
            df = pd.DataFrame([st.session_state.factura_manual])  # diccionario en variable de session a df
            st.download_button(    # boton de descarga y contiene todas las acciones que hace en su descripción
                label="Descargar CSV",   
                data=df.to_csv(index=False, encoding="utf-8-sig"), 
                file_name=(
                    f"factura_{st.session_state.factura_manual.get('Número de factura','')}.csv"
                    if st.session_state.factura_manual.get("Número de factura")
                    else "factura_valida.csv"
                ),
                mime="text/csv"  # tipo   de archivo que se descarga en este caso csv
            )
