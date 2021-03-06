from io import open
import pathlib
import shutil

# Abrir un archivo
ruta = str(pathlib.Path().absolute()) + "/mis_archivos/archivo.txt"
archivo = open(ruta,"a+")

# Escribir
archivo.write("\n ----- Este es un texto insertado desde Python -------")

# Cerrar archivo
archivo.close()

# Abrir archivo en modo solo lectura
path = str(pathlib.Path().absolute()) + "/mis_archivos/archivo.txt"
archivo_lectura = open(path,"r")

# Leer contendido
#contenido = archivo_lectura.read()
#print(contenido)

# Leer contenido y guardar en lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

for frase in lista:
  #lista_frase = frase.split
  #print(lista_frase)
  print("-" + frase.center(100))

"""
 Copiar

ruta_original = str(pathlib.Path().absolute()) + "/mis_archivos/archivo.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/mis_archivos/copia_archivo.txt"
ruta_alternativa = str(pathlib.Path().absolute()) + "/../tester/tester.txt"

shutil.copyfile(ruta_original, ruta_nueva)
"""

# Mover Archivos
"""
ruta_original = str(pathlib.Path().absolute()) + "/../tester/tester.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/mis_archivos/archivo_moved.txt"

shutil.move(ruta_original,ruta_nueva)
"""

# Eliminar Archivos

import os
"""
ruta_nueva = str(pathlib.Path().absolute()) + "/mis_archivos/archivo_moved.txt"
os.remove(ruta_nueva)
"""

# Comprobar si existe un archivo
import os.path
#ruta_comprobar = os.path.abspath("./") + "/mis_archivos/archivo_nuevo.txt"
ruta_comprobar = "./archivos.py"

if os.path.isfile(ruta_comprobar):
  print("El archivo si existe")
else:
  print("El arhivo no existe")

print(os.path.abspath("../"))
