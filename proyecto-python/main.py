"""
Proyecto de Python y MySQL

- Abrir asistente
- Login / Registro
  - Si elegimos registro, creara un usuario en la bd (base de datos)
  - Si elegimos login, idenficar usuario y preguntará
  - Crear nota, mostrar nota o borrar notas

"""
from usuarios import acciones

print("""
Acciones disponibles:
- Registro
- Login
""")

realizar = acciones.Acciones()
accion = input("¿Que acción deseas realizar?: ")

if  accion == "registro":
  realizar.registro()
elif accion == "login":
  realizar.login()