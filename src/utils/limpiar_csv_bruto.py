import io

def limpiar_csv_bruto(file):
    raw = file.read().decode("utf-8") # Convierte a cadena de texto.--> Esto permite inspeccionar y modificar línea por línea
    file.seek(0)

    lineas = raw.splitlines() #  Separa el contenido en una lista de líneas para analizarlas individualmente.
    lineas_limpias = []

    for linea in lineas:
        if linea.count('"') % 2 != 0:    # Si la linea tiene numero impar de comillas significa que hay una sin cerrar
            linea += '"'  # añadimos y cerramos comillas abiertas

        dentro_comillas = False
        nueva_linea = ""
        for char in linea:
            if char == '"':
                dentro_comillas = not dentro_comillas
            if char == "," and dentro_comillas:
                nueva_linea += ";"  # reemplazo temporal de comas internas al escrito/descripcion para que pandas no confunda con separador de columa
            else:
                nueva_linea += char

        lineas_limpias.append(nueva_linea)

    return io.StringIO("\n".join(lineas_limpias))  # Une todas las líneas corregidas en un nuevo archivo virtual
