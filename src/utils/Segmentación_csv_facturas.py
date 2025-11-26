import streamlit as st

def mostrar_facturas_por_separado(dataframe_facturas):

    st.subheader("Listado de facturas individuales")

    for numero_fila, factura in dataframe_facturas.iterrows():
        numero_factura = factura['Número de factura']

        with st.expander(f"Factura {numero_fila + 1} - {numero_factura}"):  # st.expander --> Contenedor desplegable evitar saturación de pantalla
            st.write(f"**Fecha de emisión:** {factura['Fecha de emisión']}")
            st.write(f"**Cliente:** {factura['Detalles del cliente']}")
            st.write(f"**Vendedor:** {factura['Detalles del vendedor']}")
            st.write(f"**Descripción:** {factura['Descripción de los productos o servicios']}")
            st.write(f"**Precio:** {factura['Precios de los productos o servicios']}")
            st.write(f"**Impuestos:** {factura['Impuestos aplicables']}")
            st.write(f"**Total a pagar:** {factura['Total a pagar']}")

            st.write("🔍 Validación pendiente...")