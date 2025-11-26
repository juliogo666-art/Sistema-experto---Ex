import pandas as pd

def rellenar_texto(valor, reemplazo="SIN DATOS"):
    if pd.isna(valor) or str(valor).strip() == "":
        return reemplazo
    return str(valor).strip()

def rellenar_numero(valor, reemplazo="0.0"):
    if pd.isna(valor) or str(valor).strip() == "":
        return reemplazo
    return str(valor).strip()

def limpiar_final_dataframe(df):
    df["Número de factura"] = df["Número de factura"].apply(rellenar_texto)
    df["Fecha de emisión"] = df["Fecha de emisión"].apply(rellenar_texto)
    df["Detalles del cliente"] = df["Detalles del cliente"].apply(rellenar_texto)
    df["Detalles del vendedor"] = df["Detalles del vendedor"].apply(rellenar_texto)
    df["Descripción de los productos o servicios"] = df["Descripción de los productos o servicios"].apply(rellenar_texto)

    df["Precios de los productos o servicios"] = df["Precios de los productos o servicios"].apply(rellenar_numero)
    df["Impuestos aplicables"] = df["Impuestos aplicables"].apply(rellenar_numero)
    df["Total a pagar"] = df["Total a pagar"].apply(rellenar_numero)
    return df
