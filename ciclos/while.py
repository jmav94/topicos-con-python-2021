"""
while condicion:
  ejecuta este bloque de instruccion
  actualizacion del contador / bandera

"""

contador = 1

while contador <= 20:
  print(f"Estoy en el numero {contador}")
  contador+=1

print("----------------------------------")

contador = 1
muestrame = str(0)

while contador <=100:
  #muestrame = muestrame + ", " + str(contador)
  muestrame += ", " + str(contador)
  contador += 1

print(muestrame)

print("######## Ejercicio Tablas de Multiplicar ########")

numero= int(input("Capture el numero de la tabla que quiere calcular: "))

if numero < 1:
  numero = 1

print(f"Usted selecciono la tabla del {numero}: ")

contador = 1
while contador <=10:
  print(f"{numero} x {contador} = {numero * contador}")
  contador+=1
else:
  print("Tabla terminada.")