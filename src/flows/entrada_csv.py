import streamlit as st
import pandas as pd

from utils.limpieza_falta_datos_csv import limpiar_final_dataframe 
from utils.limpiar_csv_bruto import limpiar_csv_bruto
from utils.Segmentación_csv_facturas import mostrar_facturas_por_separado
from utils.Validación_facturas import validar_factura_individual

def subir_csv():
    facturas = st.file_uploader("Sube tu CSV de facturas", type=["csv"])

    if facturas: # tenemos facturas
        # limpieza y/o tratado de datos inicial
        archivo_limpio = limpiar_csv_bruto(facturas)  # añadimos comillas faltantes y evitamos confusion de comas
        # Recogemos el csv limpio o tratado
        df = pd.read_csv(archivo_limpio, sep=",", quotechar='"', engine="python")
        
        df.columns = [col.strip() for col in df.columns]  # eliminamos  espacios en blanco delante y detras de cada nombre en cada columna
         # limpieza final --> evitamos espacios vacios
        df = limpiar_final_dataframe(df)
        
        # Vista general archivo limpio 
        st.subheader("Vista general archivo limpio")
        st.dataframe(df)

        col1, col2 = st.columns([1,1])

        with col1: 
            # Segmentación para mostrar facturas por separado
            mostrar_facturas_por_separado(df)

        with col2:
            st.subheader("Lista de facturas verificadas")
            facturas_validas = 0
            facturas_invalidas = 0

            for i, factura in df.iterrows():
                with st.expander(f"Factura{i + 1} - {factura['Número de factura']}"):
                    st.write(f"Cliente: {factura['Detalles del cliente']}")

                    # Validación
                    es_valida, errores = validar_factura_individual(factura)
                    if es_valida:
                        st.success("Factura válida")
                        facturas_validas += 1
                
                    else:
                        st.error("Factura inválida")
                        facturas_invalidas += 1
                        for error in errores:
                            st.write(f"- {error}")


        st.subheader("Resumen de validación")
        total_facturas = len(df)
        st.write(f"Total de facturas analizadas: {total_facturas}")
        st.write(f"✅ Facturas válidas: {facturas_validas}")
        st.write(f"❌ Facturas inválidas: {facturas_invalidas}")
        porcentaje_validez = round((facturas_validas / total_facturas) * 100, 2)
        st.write(f"📈 Porcentaje de cumplimiento: {porcentaje_validez}%")