"""
NoneType - None - Nada
str - String - Cadena de texto
int - Integer - Entero
float - flotante - Decimal
bool - Boolean - True/False

list - Lista - Coleccion de datos
tuple - Tuplas - Coleccion de datos estatica
dict - Diccionario - Clave y su valor
range - Rango
byte -
set - Similar a los diccionarios pero puede funcionar con variables

"""

nada = None
cadena = "Hola Juan Ahumada, tu correo es juan.ahumada94@gmail.com"
entero = 15
decimal = 25.32
boolean = True
lista = [11,12,13,14,15]
listaMixta = [11,"cadena",False,15,23.45]
tupla = ("esto","es","una","tupla")
diccionario = {
  "nombre" : "Juan",
  "apellido" : "Ahumada",
  "correo" : "juan.ahumada94@gmail.com"
}

# Impresion de valor y su tipo de dato

print(nada)
print(type(nada))

print(cadena)
print(type(cadena))

print(entero)
print(type(entero))

print(decimal)
print(type(decimal))

print(boolean)
print(type(boolean))

print(lista)
print(type(lista))

print(listaMixta)
print(type(listaMixta))

print(tupla)
print(type(tupla))

print(diccionario)
print(type(diccionario))


#Convertir de un tipo de dato a otro

texto = "un texto"
numero =2021

print(texto+" "+ str(numero)) # Esto da un error por el tipo int.
print(f"{texto} {numero}")

numero2 = float(768)
print(numero2)
print(type(numero2))

booleana = bool(0)
print(booleana)
print(type(booleana))
