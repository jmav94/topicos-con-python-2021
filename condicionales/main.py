"""
IF

SI se cumple esta condicion:
  Ejecutar estas instrucciones
SI NO:
  Se ejecutan estas otras instrucciones

if condicion:
  instrucciones
else:
  otras instrucciones

# Operadores de comparacion
== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

# Operadores Logicos
and Y
or O
! negacion
not no

"""

# Ejemplo

color = "amarillo"
#color = input("Adivina cual es mi color favorito: ")

if color == "rojo":
  print("Felicidades adivinaste el color.")
else:
  print("Este no es mi color.")

print("____________________________________________")

# ejemplo 2

anio = 2021
#anio = int(input("En que año estamos? "))

if anio < 2022:
  print("Estamos antes del 2022")
else:
  print("Es un año posterior al 2021")

print("________________________________")

# ejemplo 3 if anidados

"""
nombre = input("Captura tu nombre: ")

apellido = input("Captura tu apellido: ")

numControl = int(input("Captura tu numero de control: "))

edad = int(input("Captura tu edad: "))

semestre = int(input("Captura el semestre: "))

if semestre >= 7:
  print(f"{nombre} felicidades estas listo para elegir tu especialidad.")

  if edad >= 21:
    print("Tambien puedes realizar tu servicio social.")
  else:
    print("Por el momento no eres apto para realizar el servicio social.")
else:
  print("No estas listo para seleccionar una especialidad.")
"""

print("-----------------------------------------------------------------")

# ejemplo 4 elif

dia = int(input("Capture el numero de dia de la semana: "))

"""
if dia == 1:
  print("Lunes")
else:
  if dia == 2:
    print("Martes")
  else:
    if dia == 3:
      print("Miercoles")
    else:
      if dia == 4:
        print("Jueves")
      else:
        if dia == 5:
          print("Viernes")
        else:
          print("Es fin de semada")
"""
if dia == 1:
  print("Lunes")
elif dia == 2:
  print("Martes")
elif dia == 3:
  print("Miercoles")
elif dia == 4:
  print("Jueves")
elif dia == 5:
  print("Viernes")
else:
  print("Es fin de semada")