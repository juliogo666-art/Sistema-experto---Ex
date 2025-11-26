
# `MD047` - Introducción

 Una empresa de contabilidad nos ha solicitado el desarrollo de un sistema experto basado en reglas para facilitar la verificación  correcta de facturas y apoyar a sus contables en su trabajo diario. Este sistema experto utilizará un conjunto de reglas  predefinidas para evaluar la corrección de las facturas, lo que ayudará a garantizar la precisión y eficiencia en el proceso de verificación.
Requisitos:
 Entrada: Datos del usuario, se adjuntan datos, opción de inserción libre
 Salida: Muestra si la factura es valida o no basándose en el conocimiento experto ya introducido, también deberá mostrar su razonamiento.
Reglas:
  La factura debe incluir un número de factura único, con el siguiente formato XX-XX-XXXY. Donde X es una letra e Y es un número
  La factura debe incluir la fecha de emisión en formato YYYY-MM-DD
  La factura debe incluir los detalles del cliente y del vendedor
  La factura debe incluir una descripción de los productos o servicios no menor a 50 caracteres
  La factura debe incluir los precios de los productos o servicios en euros.
  La factura debe incluir los impuestos aplicables, siempre y cuando esos impuestos no sean negativos
  La factura debe incluir el total a pagar, que no debe ser mayor que 2000 euros
  