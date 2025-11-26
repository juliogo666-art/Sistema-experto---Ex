import streamlit as st

from flows.entrada_csv import subir_csv
from flows.entrada_manual import escribir_factura
from knowledge_base.rules import mostrar_reglas

def main():

    st.title("Verificador de facturas")

    #Requisito nº1 de entrada --> Entrada de usuario
    usuario = st.text_input("Introduce tu nombre o ID para cargar facturas")

    if usuario:

        st.success(f"Bienvenido {usuario}, ahora puedes subir o crear facutras")

        st.header("Selección y ayuda", divider=True )

        col1, col2 = st.columns([1,1])
        with col1:
            opcion = st.radio("Selecciona modo de entrada:",["Subir archivo csv","Escribir factura"])
        with col2:
            mostrar_reglas()

        if opcion == "Subir archivo csv" :
            # Requisito nº2 de entrada --> Entrada de un fichero de datos 
            st.header("Cargar CSV", divider=True )
            subir_csv()

        elif opcion == "Escribir factura":
            st.header("Escriba la factura", divider=True )
            escribir_factura()

    else:
        st.warning("Por favor, introduzca su nombre o ID")

        
if __name__ == "__main__":
    main()

