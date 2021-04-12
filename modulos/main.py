#import mimodulo
#from mimodulo import holamundo
#from mimodulo import calculadora
from mimodulo import *

nombre = "Angel Daniel Mtz Mendez"
print(holamundo(nombre))

n1 = 10
n2 = 5
basicas = True

print(calculadora(n1,n2,basicas))

# Modulo para fechas
import datetime

print(datetime.date.today())

# Fecha completa
fechaCompleta = datetime.datetime.now()
print(fechaCompleta)
print(fechaCompleta.year)
print(fechaCompleta.month)
print(fechaCompleta.day)
print(fechaCompleta.hour)

fechaPersonalizada = fechaCompleta.strftime("%d/%m/%Y, %H:%M:%S")
print("Esta es una fecha personalizada", fechaPersonalizada)

print(datetime.datetime.now().timestamp())

import math
print("Raiz cuadrada de 10: ", math.sqrt(10))

print("Numero PI: ", float(math.pi))

print("Redondear algun numero: ", math.floor(8.780945))

import random

print("este es un numero aleatorio entre 40 y 70: ", random.randint(40,70))
