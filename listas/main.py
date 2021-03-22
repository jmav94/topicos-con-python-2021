"""
Listas
Tipos de elementos en una lista
Acceder y modificar lo elementos de una lista
"""
miLista = ["uno", "dos", "tres", "cuatro", "cinco"]

print(miLista[-1])
print(miLista[-2])
print(miLista[-3])

#miLista[-1] = 14
#miLista[-1] = "String"

print(miLista[-1])


#miLista[1]
print(miLista[3:])
# ["cuatro", "cinco"]
print(miLista[1:4])
# ["dos", "tres"]
print(miLista[::-1])
# ["cinco", "cuatro", "tres", "dos", "uno"]

miLista = ['uno',[2,3,4], 'dos', 'tres']
print(miLista)

print(miLista[1])

print(miLista[1][2])

print(miLista[1][::])

print(miLista[1][1::])

miLista[3]= False

print(miLista)

# Concatenar

letras = ['A','B','C','D']
numeros = [1,2,3,4,5]

print(numeros+letras)

# Replicar Listas
numeros *=3
#numeros = numeros * 3

print(numeros)

# Metodos de las listas append, extend, pop...

letras.append(True)
print(letras)

lista = [1,2,3]
otraLista = [4,5]
lista.extend(otraLista)
# lista + otraLista
print(lista)

lista.pop()
print(lista)

lista.pop(-1)
print(lista)

lista.pop(1)
print(lista)

desordenada = [4,6,1,8,3,9,4,4]



# Metodo Insert
desordenada.insert(10,13)
# Metodo Remove
desordenada.remove(1)



desordenada.sort()
print(desordenada)

desordenada.reverse()
print(desordenada)

# Operaciones de interprete
print(len(desordenada))
print(min(desordenada))
print(max(desordenada))

# Buscar e imprimir dentro de una lista
print('D' in letras)

# Metodo count
print(desordenada.count(4))

listaTest =[1,8,5,4,2,7]

# Metodo Index
print(listaTest.index(7))

# Listas multidimensionales
print( '####### Lista de contactos ########')
contactos = [
  [
    'Juan','juan@mail.com'
  ],
  [
    'Angel','angel@gmail.com'
  ],
  [
    'Daniel','daniel@gmail.com'
  ]
]

for contacto in contactos:
  for elemento in contacto:
    if contacto.index(elemento) == 0:
      print(f'Nombre: {elemento}')
    else:
      print(f'Email: {elemento}')
  print('\n')

  print(contactos[1][1])