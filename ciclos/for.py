# for variable in iterable (lista, rango, array)
#   Instrucciones

contador = 0
restultado = 0

for contador in range(0,6):
  print("Esto es un ejmplo del ciclo for y esta la vuelta " + str(contador))
  contador +=1

print("Aqui termina el ciclo")

print("######### Ejemplo tablas de multiplicar ##############")

numero = int(input("Capture el numero de la tabla que quieres mostrar: "))

if numero < 1:
  numero =1

for numero_tabla in range(1,11):
  print(f"{numero} x {numero_tabla} = {numero * numero_tabla}")
  if numero * numero_tabla == 45:
    print("El numero es 45 y aqui tenemos un break")
    break
else:
  print("Resultado impreso completamente.")