import streamlit as st


from utils.Validación_facturas import validar_factura_individual

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
        if es_valida:
            st.success("✅ Factura válida")
        else:
            st.error("❌ Factura inválida:")
            for error in errores:
                st.write(f"- {error}")

