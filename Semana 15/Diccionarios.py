# Crear un Diccionario
informacion_personal = {
    "nombre": "Ana Pérez",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Ingeniera de Sistemas"
}
print(informacion_personal["nombre"])
print(informacion_personal["edad"])

# Acceder y Modificar Valores
print(f"Ciudad actual: {informacion_personal['ciudad']}")
informacion_personal['ciudad'] = "Guayaquil"
print(f"Ciudad modificada: {informacion_personal['ciudad']}")

# Agregar una nueva clave-valor (ya existía "profesion", pero la instrucción decía agregar)
# Si la clave ya existe, simplemente se actualiza el valor.
informacion_personal['profesion'] = "Desarrolladora de Software"
print(f"Profesión: {informacion_personal['profesion']}")

# Verificar Existencia de Claves y Agregar si no existe
if "telefono" not in informacion_personal:
    informacion_personal['telefono'] = "0991234567"
    print("La clave 'telefono' no existía, se ha agregado.")
else:
    print("La clave 'telefono' ya existe.")

# Eliminar una Clave
if "edad" in informacion_personal:
    del informacion_personal['edad']
    print("La clave 'edad' ha sido eliminada.")
else:
    print("La clave 'edad' no existe en el diccionario.")

# Imprimir el Diccionario Final
print("\nDiccionario final:")
print(informacion_personal)