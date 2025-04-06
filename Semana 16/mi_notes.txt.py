# Ejemplo de Escritura en Archivos en Python usando write() y writelines()

# Definimos el nombre del archivo
file_name = "mis_notas.txt"

# Modo de apertura: "w" para escritura (write)
archivo_escritura = open(file_name, "w")

# Método write(): escribir una línea a la vez
archivo_escritura.write("Línea 1: Hoy me levante temprano a terminar de hacer mis tareas.\n")
archivo_escritura.write("Línea 2: Hoy tengo pruebas de cada materia.\n")

# Método writelines(): escribir una lista de líneas
lineas = ["Línea 3: Hoy tuve el mejor partido el cual podría cambiar mi vida.\n", "Línea 4: Mañana empiezo los exámenes "
                                                                                  "finales.\n"]
archivo_escritura.writelines(lineas)

# Cerramos el archivo de escritura
archivo_escritura.close()

# Modo de apertura: "r" para lectura (read)
archivo_lectura = open(file_name, "r")

# Leemos y mostramos el contenido para verificar
contenido = archivo_lectura.read()
print("Contenido del archivo después de escribir:")
print(contenido)

# Cerramos el archivo de lectura
archivo_lectura.close()