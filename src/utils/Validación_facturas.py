import re

def validar_factura_individual(factura):

    errores_detectados = []

    # Regla 1: Formato del número de factura (XX-XX-XXXY)
    formato_factura = r"^[A-Z]{2}-[A-Z]{2}-[A-Z]{3}\d$"
        # ^ → inicio del texto
        # [A-Z]{2} → 2 letras mayúsculas
        # - → un guion literal
        # [A-Z]{2} → otras 2 letras mayúsculas
        # - → otro guion literal
        # [A-Z]{3} → exactamente 3 letras mayúsculas
        # \d → un dígito (número del 0 al 9)
        #  $ → fin del text

    if not re.match(formato_factura, str(factura['Número de factura']).strip()): #comprobamos que coincida el formato con establecido con el de la factura
        errores_detectados.append(" Número de factura no cumple el formato XX-XX-XXXY") # sino cumple añadimos a la lista


    # Regla 2: Fecha en formato YYYY-MM-DD
    formato_fecha = r"^\d{4}-\d{2}-\d{2}$"
        #  ^ → inicio del texto
        #  \d{4} → exactamente 4 dígitos (el año, ej. 2025)
        #  - → guion
        #  \d{2} → exactamente 2 dígitos (el mes, ej. 11)
        #  - → guion
        #  \d{2} → exactamente 2 dígitos (el día, ej. 23)
        #  $ → fin del text

    if not re.match(formato_fecha, str(factura['Fecha de emisión']).strip()):
        errores_detectados.append(" Fecha no está en formato YYYY-MM-DD")

    # Regla 3: Cliente y vendedor deben estar presentes
    if not factura['Detalles del cliente'] or not factura['Detalles del vendedor']:
        errores_detectados.append(" Faltan datos del cliente o del vendedor")

    # Regla 4: Descripción mínima de 50 caracteres
    descripcion = str(factura['Descripción de los productos o servicios']).strip()
    if len(descripcion) < 50:
        errores_detectados.append(" Descripción demasiado corta (menos de 50 caracteres)")

    # Regla 5: La factura debe estar en euros, es decir comprobamos que tengan el simbolo € en las columnas monetarias
    columnas_monetarias = [
        'Precios de los productos o servicios',
        'Impuestos aplicables',
        'Total a pagar'
    ]
    for columna in columnas_monetarias:
        valor = str(factura[columna]).strip()
        if "€" not in valor:
            errores_detectados.append(f" Falta el símbolo € en la columna: {columna}")

    # Regla 6: Impuestos deben estar presentes y no ser negativos

    try:
        impuestos_limpios = float(str(factura['Impuestos aplicables']).replace("€", "").replace(",", ".").strip())
        if impuestos_limpios < 0:
            errores_detectados.append(" Impuestos negativos")
    except ValueError:
        errores_detectados.append(" Impuestos no son un valor numérico válido")

    # Regla 7: Total no debe superar los 2000€

    try:
        total_limpio = float(str(factura['Total a pagar']).replace("€", "").replace(",", ".").strip())
        if total_limpio > 2000:
            errores_detectados.append(" El total a pagar supera los 2000€")
    except ValueError:
        errores_detectados.append(" Total a pagar no es un valor numérico válido")

    ################################################
    
    es_valida = len(errores_detectados) == 0
    return es_valida, errores_detectados
