import os, shutil

# Crear carpeta
if not os.path.isdir("./carpeta_nueva"):
  os.mkdir("./carpeta_nueva")
else:
  print("Esta carpeta ya existe")

# Copiar carpeta
"""
ruta_original = "./carpeta_nueva"
ruta_nueva = "./carpeta_copy"

shutil.copytree(ruta_original,ruta_nueva)
"""

# Eliminar carpetas
#os.rmdir('./carpeta_copy')
#shutil.rmtree('./carpeta_copy')

print("Imprimiendo contenido de carpeta")
contenido = os.listdir("./carpeta_copy")

for elemento in contenido:
  print("elemento: " + elemento)