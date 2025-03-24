# Crea una función llamada calcular_descuento que tome dos parámetros: el monto total de la compra y un valor predeterminado para el porcentaje de descuento (por ejemplo, 10% por defecto).
#
# La función debe calcular el descuento aplicando el porcentaje al monto total de la compra.
#
# La función debe devolver el monto del descuento calculado.
def calcular_descuento(valor_total, porcentaje_descuento=30):
    desuento = valor_total * (porcentaje_descuento/100)
    return desuento
if __name__ == '__main__':
    valor1 = 1200
    valor2 = 3400
# llamo a la funcion
    descuento1 = calcular_descuento(valor1)
    print(f"El valor de tu compra es {valor1}, y el descuento es de {descuento1}")

# llamo a la funcion
    porcentaje_descuento = 60
    descuento2 = calcular_descuento(valor2)
print(f"El valor de tu compra es {valor2}, y el descuento es de {descuento2}")
