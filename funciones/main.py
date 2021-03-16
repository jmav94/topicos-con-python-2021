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

#nombre = input("Captura tu nombre: ")
#edad = int(input("Captura tu edad: "))

nombre = "Jorge"
edad = 20

mostrarNombre(nombre,edad)

print("###### Ejemplo tabla de multiplicar ######")

def tabla(numero):
  print(f"Tabla de multiplicar del numero {numero}: ")

  for contador in range(1,11):
    operacion = numero * contador
    print(f"{numero} X {contador} = {operacion}")

  print("\n")

tabla(3)
tabla(5)
#tabla(8)
#tabla(10)

print("####### Tablas del 1 al 10 ##########")

for numeroTabla in range(1,11):
  tabla(numeroTabla)

print("####### Parametro opcionales ########")

def consultarEmpleado(nombre = "Roberto Mtz", nidentificacion = None):
  print("Empleado")
  print(f"{nombre}")

  if nidentificacion != None:
    print(f"{nidentificacion}")

consultarEmpleado("Juan Perez")
consultarEmpleado("Daniel Hdz", 28394)
consultarEmpleado(nidentificacion=23948239)
consultarEmpleado(nidentificacion=000000, nombre="Otro nombre")
consultarEmpleado()


print("##### Ejemplo con return ######")

def saludar(nombre):
  saludo = f"Hola {nombre}, bienvenido!!"

  return saludo

print(saludar("Angel Reyes"))

print("##### Funciones que llaman a otras funciones ######")

def getNombre(nombre):
  texto = f"El nombre es {nombre}"
  return texto

def getApellido(apellido):
  texto = f"El apellido es {apellido}"
  return texto

def getEdad(edad):
  texto = f"Su edad es de {edad} años"
  return texto

def devolverTodo(nombre,apellido,edad):
  texto = getNombre(nombre) + "\n" + getApellido(apellido) + "\n" + getEdad(edad)
  return texto

print(devolverTodo(nombre="Luis", apellido="Castillo",edad=25))

print("####### Funcion lambda #########")

dameElAnio = lambda year: year*50

print(dameElAnio(2021))