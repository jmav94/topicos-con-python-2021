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

print("########### condicionales comparando enteros con operadores relacionales ###############")

# ejemplo 2

anio = 2021
#anio = int(input("En que año estamos? "))

if anio < 2022:
  print("Estamos antes del 2022")
else:
  print("Es un año posterior al 2021")

print("________________________________")

# ejemplo 3 if anidados


"""nombre = input("Captura tu nombre: ")

apellido = input("Captura tu apellido: ")

numControl = int(input("Captura tu numero de control: "))

edad = int(input("Captura tu edad: "))

semestre = int(input("Captura el semestre: "))"""

nombre = "Juan"

apellido = "Perez"

numControl = 20100105

edad = 23

semestre = 9

if semestre >= 7:
  print(f"{nombre} felicidades estas listo para elegir tu especialidad.")

  if edad >= 21:
    print("Tambien puedes realizar tu servicio social.")
  else:
    print("Por el momento no eres apto para realizar el servicio social.")
else:
  print("No estas listo para seleccionar una especialidad.")


print("############## ejemplo con elif ##################")

# ejemplo 4 elif

#dia = int(input("Capture el numero de dia de la semana: "))
dia = 2
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

print("######## ejemplo edades - operadores realacionales y AND #########")

edad_minima = 18
edad_maxima = 65

# input de usuario
#edad = int(input("¿Tienes edad para trabajar? Captura tu edad: "))
edad = 38
if edad >= edad_minima and edad <= edad_maxima:
  print("Estas en edad para trabajar.")
else:
  print("No estas en edad para trabajar.")


print("######## ejemplo operadores relacionales y logicos con condicionales #########")

pais = "Mexico"
#pais = input("Capture el pais que desee validar: ")

if pais == "Mexico" or pais == "España" or pais == "Colombia":
  print("En este pais se habla español")
else:
  print("En este pais no se habla español")

print("######## ejemplo operadores relacionales y logicos con condicionales + not #########")

pais = "Mexico"
#pais = input("Capture el pais que desee validar: ")

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
  print(f"{pais} En este pais no se habla español")
else:
  print(f"{pais} En este pais se habla español")

print("######## ejemplo operadores relacionales - !=  #########")

pais = input("Capture el pais que desee validar: ")

if pais != "Mexico" and pais != "España" and pais != "Colombia":
  print(f"{pais} En este pais no se habla español")
else:
  print(f"{pais} En este pais se habla español")