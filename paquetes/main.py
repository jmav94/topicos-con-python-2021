"""
Los paquetes peuden contener modulos y otros paquetes. Estos son otros directorios (carpetas). El unico requisito es que contengan un archivo llamado __init__.py. Este archivo puede incluso estar vacio.
"""

print("Aprendiendo de Paquetes en Python: ")

from mipaquete import herramientas, pruebas

pruebas.probando()

herramientas.nombreCompleto("Juan", "Ahumada Vazquez")