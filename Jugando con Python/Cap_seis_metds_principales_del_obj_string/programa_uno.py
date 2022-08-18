# Comentario simple de una solo línea de código
"""Comentario de varias líneas de código
Línea 1
Línea 2
Línea 3
Línea n"""

monto_bruto = 175
tasa_interes = 12
monto_interes = monto_bruto * tasa_interes / 100
tasa_bonificacion = 5
importe_bonificacion = monto_bruto * tasa_bonificacion / 100
monto_neto = (monto_bruto - importe_bonificacion) + monto_interes

print(f"El monto neto es {monto_neto}")