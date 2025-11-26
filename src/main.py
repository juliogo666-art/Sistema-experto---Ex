import io
import streamlit as st
import pandas as pd
import csv

from flows.entrada_csv import subir_csv
from flows.entrada_manual import escribir_factura

def main():

    st.title("Verificador de facturas")

    #Requisito nº1 de entrada --> Entrada de usuario
    usuario = st.text_input("Introduce tu nombre o ID para cargar facturas")

    if usuario:

        st.success(f"Bienvenido {usuario}, ahora puedes subir o crear facutras")

        opcion = st.radio("Selecciona modo de entrada:",["Subir archivo csv","Escribir factura"])
        
        if opcion == "Subir archivo csv" :
            # Requisito nº2 de entrada --> Entrada de un fichero de datos 
            subir_csv()

        elif opcion == "Escribir factura":
            escribir_factura()

    else:
        st.warning("Por favor, introduzca su nombre o ID")

        
if __name__ == "__main__":
    main()

