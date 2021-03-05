"""
def nombreFuncion(parametros):
  print("Esta es una funcion.")
  # bloque de instrucciones

nombreFuncion(mi_parametro)
nombreFuncion(otro_parametro)
"""

print("##### Ejemplo Basico sin parametros #######")
# Definir funcion
def mostrarDatos():
  print("Pedro")
  print("Alejandra")
  print("Francisco")
  print("Daniela")
  print("\n")

# Invocar funcion
mostrarDatos()
mostrarDatos()
mostrarDatos()

print("#### Ejemplo funcionces con parametros ####")

def mostrarNombre(nombre, edad):
  print(f"Tu nombre es: {nombre}")

  if edad <= 18:
    print("Y eres menor de edad.")
  else:
    print("Y eres mayor de edad")

nombre = input("Captura tu nombre: ")
edad = int(input("Captura tu edad: "))
mostrarNombre(edad,nombre)

